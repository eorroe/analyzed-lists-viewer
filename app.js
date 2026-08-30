const REPO_OWNER = 'eorroe';
const REPO_NAME = 'analyzed-lists-viewer';
const RAW_BASE = `https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/main`;
const TREES_API_BASE = `https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/git/trees`;
const CACHE_TTL_MS = 24 * 60 * 60 * 1000;
const THEME_KEY = 'lists-viewer-theme';

const getTheme = () => {
    return localStorage.getItem(THEME_KEY) || 'dark';
};

const setTheme = (theme) => {
    localStorage.setItem(THEME_KEY, theme);
    document.documentElement.setAttribute('data-theme', theme);
};

const toggleTheme = () => {
    const current = getTheme();
    const themes = ['dark', 'light', 'sepia'];
    const currentIndex = themes.indexOf(current);
    const nextIndex = (currentIndex + 1) % themes.length;
    setTheme(themes[nextIndex]);
};

const initTheme = () => {
    setTheme(getTheme());
};

const REPO_TREE_CACHE_KEY = 'repo-tree';
const SOURCE_LIST_CACHE_KEY = 'source-list';
const LIST_INDEX_CACHE_KEY = 'list-index';
const LISTS_QUOTES_CACHE_KEY = 'lists-quotes';

let currentPath = '';
let selectedItem = null;
let isLoading = false;
let db = null;
let currentFiles = [];
let rootListSearch = '';
let searchBody = false;
let currentQuote = '';

const isOnline = () => navigator.onLine;

const debounce = (fn, ms) => {
    let timer;
    return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), ms);
    };
};

const elements = {
    loading: document.getElementById('loading'),
    error: document.getElementById('error'),
    mainContent: document.getElementById('main-content'),
    breadcrumb: document.getElementById('breadcrumb'),
    breadcrumbPath: document.getElementById('breadcrumb-path'),
    breadcrumbHome: document.getElementById('breadcrumb-home'),
    breadcrumbSource: document.getElementById('breadcrumb-source'),
    breadcrumbPathSeparator: document.getElementById('breadcrumb-path-separator'),
    retryBtn: document.getElementById('retry-btn'),
    themeToggle: document.getElementById('theme-toggle')
};

const openCacheDb = () => {
    return new Promise((resolve, reject) => {
        const request = indexedDB.open('lists-viewer-cache', 1);
        request.onupgradeneeded = (event) => {
            const database = event.target.result;
            if (!database.objectStoreNames.contains('cache')) {
                database.createObjectStore('cache', { keyPath: 'key' });
            }
        };
        request.onsuccess = (event) => resolve(event.target.result);
        request.onerror = (event) => reject(event.target.error);
    });
};

const getCachedItem = async (key) => {
    if (!db) return null;
    return new Promise((resolve, reject) => {
        const transaction = db.transaction(['cache'], 'readonly');
        const store = transaction.objectStore('cache');
        const request = store.get(key);
        request.onsuccess = () => {
            const result = request.result;
            if (!result) {
                resolve(null);
                return;
            }
            if (!isOnline()) {
                resolve(result.value);
                return;
            }
            const age = Date.now() - (result.timestamp || 0);
            if (age > CACHE_TTL_MS) {
                resolve(null);
                return;
            }
            resolve(result.value);
        };
        request.onerror = () => reject(request.error);
    });
};

const setCachedItem = async (key, value) => {
    if (!db) return;
    return new Promise((resolve, reject) => {
        const transaction = db.transaction(['cache'], 'readwrite');
        const store = transaction.objectStore('cache');
        const request = store.put({ key, value, timestamp: Date.now() });
        request.onsuccess = () => resolve();
        request.onerror = () => reject(request.error);
    });
};

const isMarkdownFile = (name) => typeof name === 'string' && name.toLowerCase().endsWith('.md');

const getDisplayName = (name) => {
    if (typeof name !== 'string') return name;
    const lower = name.toLowerCase();
    if (lower.endsWith('.md')) {
        return name.slice(0, -3);
    }
    return name;
};

const fuzzyMatch = (query, text) => {
    if (!query) return true;
    const lowerQuery = query.toLowerCase();
    const lowerText = text.toLowerCase();

    if (lowerText.includes(lowerQuery)) return true;

    let queryIndex = 0;
    for (let i = 0; i < lowerText.length && queryIndex < lowerQuery.length; i++) {
        if (lowerText[i] === lowerQuery[queryIndex]) {
            queryIndex++;
        }
    }
    return queryIndex === lowerQuery.length;
};

const renderSearchInput = (placeholder, id) => {
    return `
        <div class="search-container">
            <div class="search-input-wrapper">
                <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                </svg>
                <input type="text" class="search-input" id="${id}" placeholder="${placeholder}" autocomplete="off">
            </div>
            <button id="${id}-body-toggle" class="search-toggle-btn hidden" data-search-id="${id}">Searching Titles Only</button>
        </div>
    `;
};

const filterFiles = (query) => {
    if (!query) return currentFiles;
    return currentFiles.filter(file => fuzzyMatch(query, getDisplayName(file.name)));
};

const searchInBodies = async (query, files) => {
    if (!query || files.length === 0) return files;
    const lowerQuery = query.toLowerCase();
    const bodies = await Promise.all(files.map(async (file) => {
        try {
            return await fetchFileContent(file.path);
        } catch {
            return '';
        }
    }));
    return files.filter((file, i) => {
        const body = (bodies[i] || '').toLowerCase();
        return body.includes(lowerQuery);
    });
};

const renderFileButtons = (files, path) => {
    return files.map(file => {
        const subpath = file.subpath ? file.subpath + '/' : '';
        const filePath = path ? `${path}/${subpath}${file.name}` : file.name;
        return `
            <button class="folder-btn fade-in" data-path="${filePath}" data-type="file">
                <span>${escapeHtml(getDisplayName(file.name))}</span>
            </button>
        `;
    }).join('');
};

const BIBLE_BOOKS = [
    'Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy',
    'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings',
    '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job',
    'Psalms', 'Psalm', 'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Isaiah',
    'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos',
    'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai',
    'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans',
    '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians',
    'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy',
    'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John',
    '2 John', '3 John', 'Jude', 'Revelation'
].sort((a, b) => b.length - a.length);

const ESCAPED_BOOKS = BIBLE_BOOKS.map((book) =>
    book.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&')
);

const REFERENCE_PATTERN = new RegExp(
    '\\b(?:' + ESCAPED_BOOKS.join('|') + ')\\s+\\d+(?::\\d+)?(?:[\\-–—]\\d+)?\\b',
    'gi'
);

const buildBibleRefUrl = (reference) => {
    const cleaned = reference.replace(/^[.,;:!?'")\]]+|[.,;:!?'")\]]+$/g, '').trim();
    const normalized = cleaned.replace(/[–—]/g, '-');
    const match = normalized.match(/^(.+?)\s+(\d+)(?::(\d+))?(?:-(\d+))?$/);
    if (!match) {
        console.log('buildBibleRefUrl failed to parse:', { reference, cleaned, normalized });
        return null;
    }

    const [, book, chapter, verseStart, verseEnd] = match;
    const bookSlug = book.trim().replace(/\s+/g, '-');
    const chapterNum = chapter;

    if (verseStart && verseEnd) {
        const search = book.trim().replace(/\s+/g, '_') + '_' + chapterNum + ':' + verseStart + '-' + verseEnd;
        return 'https://www.bibleref.com/biblepassage/?search=' + encodeURIComponent(search);
    }

    if (verseStart) {
        return 'https://www.bibleref.com/' + encodeURIComponent(bookSlug) + '/' + chapterNum + '/' + encodeURIComponent(bookSlug + '-' + chapterNum + '-' + verseStart) + '.html';
    }

    if (verseEnd) {
        const search = book.trim().replace(/\s+/g, '_') + '_' + chapterNum + '-' + verseEnd;
        return 'https://www.bibleref.com/biblepassage/?search=' + encodeURIComponent(search);
    }

    return 'https://www.bibleref.com/' + encodeURIComponent(bookSlug) + '/' + chapterNum + '/' + encodeURIComponent(bookSlug + '-chapter-' + chapterNum) + '.html';
};

const linkifyBiblicalReferences = (text) => {
    return text.replace(REFERENCE_PATTERN, (match) => {
        const url = buildBibleRefUrl(match);
        if (url) {
            return '<a href="' + url + '" target="_blank" rel="noopener noreferrer" class="bibleref-link">' + match + '</a>';
        }
        return match;
    });
};

const getFolderIcon = () => {
    return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>`;
};

const getFilterIcon = () => {
    return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/></svg>`;
};

const getDisabledSources = () => {
    try {
        const stored = localStorage.getItem('disabledSources');
        if (stored) {
            return new Set(JSON.parse(stored));
        }
    } catch (e) {
        console.error('Failed to read disabled sources:', e);
    }
    return null;
};

const saveDisabledSources = (disabledSet) => {
    try {
        if (disabledSet === null || disabledSet.size === 0) {
            localStorage.removeItem('disabledSources');
        } else {
            localStorage.setItem('disabledSources', JSON.stringify([...disabledSet]));
        }
    } catch (e) {
        console.error('Failed to save disabled sources:', e);
    }
};

const isSourceDisabled = (sourceName) => {
    const disabled = getDisabledSources();
    return disabled === null ? false : disabled.has(sourceName);
};

const showLoading = () => {
    elements.loading.classList.remove('hidden');
    elements.error.classList.add('hidden');
    elements.mainContent.innerHTML = '';
};

const hideLoading = () => {
    elements.loading.classList.add('hidden');
};

const showError = (message) => {
    elements.loading.classList.add('hidden');
    elements.error.classList.remove('hidden');
    elements.error.querySelector('p').textContent = message;
};

const hideError = () => {
    elements.error.classList.add('hidden');
};

const hideFilterHint = () => {
    const filterHint = document.getElementById('filter-hint');
    if (filterHint) filterHint.classList.add('hidden');
};

const enterSubView = (path) => {
    currentPath = path;
    renderBreadcrumb(path);
    hideFilterHint();
};

const renderBreadcrumb = (path) => {
    if (path) {
        elements.breadcrumb.classList.remove('hidden');

        const segments = path.split('/');
        const sourceName = segments[0];
        const restOfPath = segments.slice(1).join('/');

        elements.breadcrumbSource.textContent = sourceName;
        elements.breadcrumbSource.classList.remove('hidden');

        if (restOfPath) {
            elements.breadcrumbPathSeparator.classList.remove('hidden');
            elements.breadcrumbPath.textContent = '/ ' + restOfPath;
        } else {
            elements.breadcrumbPathSeparator.classList.add('hidden');
            elements.breadcrumbPath.textContent = '';
        }
    } else {
        elements.breadcrumb.classList.add('hidden');
    }
};

const renderFolders = (folders, path) => {
    if (folders.length === 0) return '';

    const disabled = getDisabledSources();
    const filteredFolders = folders.filter(folder => {
        if (disabled === null) return true;
        return !disabled.has(folder.name);
    });

    const folderHtml = filteredFolders.map(folder => {
        const folderPath = path ? `${path}/${folder.name}` : folder.name;
        return `
            <button class="folder-btn fade-in" data-path="${folderPath}" data-type="folder">
                ${getFolderIcon()}
                <span>${escapeHtml(folder.name)}</span>
            </button>
        `;
    }).join('');

    const query = rootListSearch || '';
    const baseFiltered = query ? filterFiles(query) : currentFiles;
    const filteredFiles = disabled === null ? baseFiltered : baseFiltered.filter(file => {
        const source = file.source || (file.subpath ? file.subpath.split('/')[0] : '');
        return !disabled.has(source);
    });
    const listHtml = filteredFiles.map(file => {
        const prefix = file.source ? `${file.source}/` : '';
        const subpathPart = file.subpath ? `${file.subpath}/` : '';
        const filePath = `${prefix}${subpathPart}${file.name}`;
        const sourceLabel = file.source || (file.subpath ? file.subpath.split('/')[0] : '');
        return `
            <button class="folder-btn fade-in" data-path="${escapeHtml(filePath)}" data-type="file">
                <span>${escapeHtml(getDisplayName(file.name))}${sourceLabel ? ' <span style="opacity:0.6;font-size:0.85em">(' + escapeHtml(sourceLabel) + ')</span>' : ''}</span>
            </button>
        `;
    }).join('');

    const showLists = query.trim().length > 0;

    return `
        <div class="mb-8">
            <div class="flex justify-between items-center mb-4 border-b border-[#c5a059]/30 pb-2">
                <div class="flex items-center gap-2">
                    <button id="filter-sources-btn" class="filter-btn" title="Filter Sources of Lists">
                        ${getFilterIcon()}
                        <span class="filter-btn-text">Filter Sources of Lists</span>
                    </button>
                    <h2 class="font-['Cinzel'] text-xl text-[var(--heading)]">Select Source of List</h2>
                </div>
                <button id="check-new-source-btn" class="check-new-btn">Check For New Source of List</button>
            </div>
            ${renderSearchInput('Search all lists...', 'root-list-search')}
            <div id="source-list-container" class="source-list flex flex-col gap-2 ${showLists ? 'hidden' : ''}">
                ${folderHtml || '<p class="text-[var(--heading)] italic">No Sources of List match your filter.</p>'}
            </div>
            <div id="list-list-container" class="source-list flex flex-col gap-2 ${showLists ? '' : 'hidden'}">
                ${listHtml || '<p class="text-[var(--heading)] italic">No matching lists found.</p>'}
            </div>
        </div>
    `;
};

const renderFiles = (files, path) => {
    const markdownFiles = files.filter((file) => isMarkdownFile(file.name));
    currentFiles = markdownFiles;

    if (markdownFiles.length === 0) {
        return `
            <div class="empty-state">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>
                <h2>No Lists Found</h2>
                <p>This Source of List contains no lists yet.</p>
            </div>
        `;
    }

    const fileHtml = markdownFiles.map(file => {
        const subpath = file.subpath ? file.subpath + '/' : '';
        const filePath = path ? `${path}/${subpath}${file.name}` : file.name;
        return `
            <button class="folder-btn fade-in" data-path="${filePath}" data-type="file">
                <span>${escapeHtml(getDisplayName(file.name))}</span>
            </button>
        `;
    }).join('');

    return `
        <div class="mb-8">
            <div class="flex justify-between items-center mb-4 border-b border-[#c5a059]/30 pb-2">
                <h2 class="font-['Cinzel'] text-xl text-[var(--heading)]">Select List</h2>
                <button id="check-new-lists-btn" class="check-new-btn">Check For New Lists</button>
            </div>
            ${renderSearchInput('Search lists...', 'list-search')}
            <div id="list-list-container" class="source-list flex flex-col gap-2">
                ${fileHtml}
            </div>
        </div>
    `;
};

const renderMarkdown = (content) => {
    let html = marked.parse(content, { breaks: true, gfm: true });
    html = html.replace(/<a\s+([^>]*?)>/gi, (match, attrs) => {
        if (/\btarget=/.test(attrs)) return match;
        return `<a ${attrs} target="_blank" rel="noopener noreferrer">`;
    });
    const linkedHtml = linkifyBiblicalReferences(html);
    return `
        <div class="markdown-body fade-in">
            ${linkedHtml}
        </div>
    `;
};

const renderEmptyState = (message) => {
    return `
        <div class="empty-state">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>
            <h2>Scriptorium</h2>
            <p>${message}</p>
        </div>
    `;
};

const escapeHtml = (text) => {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
};

const updateSelectedState = (clickedElement) => {
    if (selectedItem && selectedItem !== clickedElement) {
        selectedItem.classList.remove('selected');
    }
    selectedItem = clickedElement;
    if (selectedItem) {
        selectedItem.classList.add('selected');
    }
};

const fetchFileContent = async (path, skipCache = false) => {
    const cacheKey = `file:${path}`;
    if (!skipCache) {
        const cached = await getCachedItem(cacheKey);
        if (cached) {
            return cached;
        }
    }

    const url = `${RAW_BASE}/${encodeURIComponent(path)}?t=${Date.now()}`;
    const response = await fetch(url);

    if (!response.ok) {
        throw new Error(`Failed to fetch file content: ${response.status} ${response.statusText}`);
    }

    const text = await response.text();
    await setCachedItem(cacheKey, text);
    return text;
};

const buildRepoCache = async (treeData) => {
    const items = treeData.tree || [];
    const sources = [];
    const lists = [];

    for (const item of items) {
        if (item.type === 'tree') {
            const firstSlash = item.path.indexOf('/');
            if (firstSlash === -1) {
                sources.push({
                    name: item.path,
                    path: item.path,
                    sha: item.sha,
                    size: 0,
                    type: 'dir'
                });
            }
        } else if (item.type === 'blob' && isMarkdownFile(item.path)) {
            const firstSlash = item.path.indexOf('/');
            if (firstSlash === -1) continue;

            const sourcePath = item.path.slice(0, firstSlash);
            const relativePath = item.path;
            const lastSlash = relativePath.lastIndexOf('/');
            const subpath = lastSlash === -1 ? '' : relativePath.slice(sourcePath.length + 1, lastSlash);
            const name = lastSlash === -1 ? relativePath : relativePath.slice(lastSlash + 1);

            lists.push({
                name,
                path: relativePath,
                subpath,
                source: sourcePath,
                sha: item.sha,
                size: item.size,
                type: 'file'
            });
        }
    }

    await setCachedItem(REPO_TREE_CACHE_KEY, treeData);
    await setCachedItem(SOURCE_LIST_CACHE_KEY, sources);
    await setCachedItem(LIST_INDEX_CACHE_KEY, lists);
};

const fetchRepoTree = async (skipCache = false) => {
    if (!skipCache) {
        const cachedTree = await getCachedItem(REPO_TREE_CACHE_KEY);
        if (cachedTree) return cachedTree;
    }

    if (!navigator.onLine) {
        throw new Error('You are currently offline. Please check your internet connection.');
    }

    await new Promise(resolve => setTimeout(resolve, 5000));

    const url = `${TREES_API_BASE}/main?recursive=1&t=${Date.now()}`;
    const response = await fetch(url, {
        headers: {
            'Accept': 'application/vnd.github+json'
        }
    });

    if (!response.ok) {
        throw new Error(`GitHub API error: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    if (data.truncated) {
        console.warn('Repo tree was truncated by GitHub. Some files may not be available.');
    }

    await buildRepoCache(data);
    return data;
};

const getCachedSourceList = async (skipCache = false) => {
    if (!skipCache) {
        const cached = await getCachedItem(SOURCE_LIST_CACHE_KEY);
        if (cached) return cached;
    }

    const tree = await fetchRepoTree(skipCache);
    if (!tree) return [];

    const cached2 = await getCachedItem(SOURCE_LIST_CACHE_KEY);
    return cached2 || [];
};

const getCachedListIndex = async (skipCache = false) => {
    if (!skipCache) {
        const cached = await getCachedItem(LIST_INDEX_CACHE_KEY);
        if (cached) return cached;
    }

    const tree = await fetchRepoTree(skipCache);
    if (!tree) return [];

    const cached2 = await getCachedItem(LIST_INDEX_CACHE_KEY);
    return cached2 || [];
};

const loadRootDirectories = async (skipCache = false) => {
    if (isLoading) return;
    isLoading = true;

    currentPath = '';
    selectedItem = null;
    rootListSearch = '';
    searchBody = false;
    hideError();
    showLoading();
    renderBreadcrumb('');

    try {
        const sources = await getCachedSourceList(skipCache);
        const allLists = await getCachedListIndex(skipCache);
        currentFiles = allLists;

        if (sources.length === 0) {
            hideLoading();
            elements.mainContent.innerHTML = renderEmptyState(
                'The repository is empty. Add markdown files to get started.'
            );
            const filterHint = document.getElementById('filter-hint');
            if (filterHint) filterHint.classList.remove('hidden');
            return;
        }

        let html = '';
        if (sources.length > 0) {
            html += renderFolders(sources, '');
        }

        hideLoading();
        elements.mainContent.innerHTML = html;
        const filterHint = document.getElementById('filter-hint');
        if (filterHint) filterHint.classList.remove('hidden');
        showQuote();
    } catch (error) {
        hideLoading();
        showError(error.message);
    } finally {
        isLoading = false;
    }
};

const loadLists = async (path, skipCache = false) => {
    if (isLoading) return;
    isLoading = true;

    currentPath = path;
    selectedItem = null;
    searchBody = false;
    hideError();
    showLoading();

    try {
        const allLists = await getCachedListIndex(skipCache);
        const prefix = `${path}/`;
        const files = allLists.filter(list => list.path.startsWith(prefix));

        hideLoading();

        if (files.length === 0) {
            elements.mainContent.innerHTML = renderEmptyState(
                'This Source of List has no lists yet.'
            );
            return;
        }

        currentFiles = files;
        elements.mainContent.innerHTML = renderFiles(files, path);
        showQuote();
    } catch (error) {
        hideLoading();
        showError(error.message);
    } finally {
        isLoading = false;
    }
};

const loadMarkdownFile = async (path) => {
    if (isLoading) return;
    isLoading = true;

    selectedItem = null;
    hideError();
    showLoading();

    try {
        const content = await fetchFileContent(path);
        hideLoading();
        elements.mainContent.innerHTML = renderMarkdown(content);
        hideQuote();
    } catch (error) {
        hideLoading();
        showError(`Failed to load file: ${error.message}`);
    } finally {
        isLoading = false;
    }
};

const handleItemClick = async (event) => {
    const button = event.target.closest('button');
    if (!button) return;

    const type = button.dataset.type;
    const path = button.dataset.path;

    if (!path) return;

    updateSelectedState(button);

    if (type === 'folder') {
        enterSubView(path);
        await loadLists(path);
    } else if (type === 'file') {
        const segments = path.split('/');
        const sourcePath = segments[0];
        enterSubView(sourcePath);
        await loadMarkdownFile(path);
    }
};

const handleRetry = () => {
    if (currentPath) {
        enterSubView(currentPath);
        loadLists(currentPath);
    } else {
        loadRootDirectories();
    }
};

const handleHomeClick = () => {
    loadRootDirectories();
};

const handleSourceClick = () => {
    const segments = currentPath.split('/');
    const sourcePath = segments[0];
    enterSubView(sourcePath);
    loadLists(sourcePath);
};

const handleCheckNewSource = async () => {
    if (isLoading) return;
    const btn = document.getElementById('check-new-source-btn');
    if (!btn) return;

    btn.disabled = true;
    btn.classList.add('loading');
    btn.textContent = 'Checking...';

    try {
        await loadRootDirectories(true);
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.classList.remove('loading');
            btn.textContent = 'Check For New Source of List';
        }
    }
};

const handleCheckNewLists = async () => {
    if (isLoading || !currentPath) return;
    const btn = document.getElementById('check-new-lists-btn');
    if (!btn) return;

    btn.disabled = true;
    btn.classList.add('loading');
    btn.textContent = 'Checking...';

    try {
        await loadLists(currentPath, true);
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.classList.remove('loading');
            btn.textContent = 'Check For New Lists';
        }
    }
};

const openFilterPopup = async () => {
    const popup = document.getElementById('source-filter-popup');
    if (!popup) return;
    await renderFilterPopup();
    popup.classList.remove('hidden');
};

const closeFilterPopup = () => {
    const popup = document.getElementById('source-filter-popup');
    if (popup) {
        popup.classList.add('hidden');
    }
};

const enableAllSources = async () => {
    saveDisabledSources(new Set());
    await renderFilterPopup();
    if (currentPath === '') {
        loadRootDirectories();
    } else {
        loadLists(currentPath);
    }
};

const disableAllSources = async () => {
    const sources = await getCachedSourceList();
    const allNames = new Set(sources.map(c => c.name));
    saveDisabledSources(allNames);
    await renderFilterPopup();
    loadRootDirectories();
};

const renderFilterPopup = async () => {
    const listContainer = document.getElementById('source-filter-list');
    if (!listContainer) return;

    const sources = await getCachedSourceList();

    const disabled = getDisabledSources();

    listContainer.innerHTML = `
        <div class="filter-action-btns">
            <button id="enable-all-btn" class="filter-action-btn">Enable All</button>
            <button id="disable-all-btn" class="filter-action-btn">Disable All</button>
        </div>
    ` + sources.map(source => {
        const isDisabled = disabled === null ? false : disabled.has(source.name);
        return `
            <div class="source-filter-item">
                <span class="source-filter-name">${escapeHtml(source.name)}</span>
                <label class="toggle-switch">
                    <input type="checkbox" ${isDisabled ? '' : 'checked'} data-source="${escapeHtml(source.name)}">
                    <span class="toggle-slider"></span>
                </label>
            </div>
        `;
    }).join('') || '<p class="text-[var(--heading)] italic">No Sources of List found.</p>';
};

const handleFilterToggle = async (sourceName, checked) => {
    let disabled = getDisabledSources();

    if (disabled === null) {
        disabled = new Set();
    }

    if (checked) {
        disabled.delete(sourceName);
    } else {
        disabled.add(sourceName);
    }

    saveDisabledSources(disabled);

    if (currentPath === '') {
        loadRootDirectories();
    } else {
        const segments = currentPath.split('/');
        if (segments[0] && isSourceDisabled(segments[0])) {
            loadRootDirectories();
        }
    }
};

const createDevPanel = () => {
    const main = document.querySelector('main');
    if (!main) return null;

    main.style.display = 'flex';

    const panel = document.createElement('div');
    panel.id = 'dev-panel';
    panel.className = 'dev-panel';

    panel.innerHTML = `
        <h3 class="font-['Cinzel'] text-xl text-[var(--heading)] mb-4">Developer Options:</h3>
        <button id="dev-delete-idb" class="dev-btn dev-btn-danger mb-2">CLEAR AND DELETE ALL CACHED DATA</button>
        <button id="dev-delete-localstorage" class="dev-btn dev-btn-danger mb-2">CLEAR AND DELETE ALL LOCAL STORAGE</button>
        <button id="dev-clear-sw-cache" class="dev-btn dev-btn-danger">CLEAR SERVICE WORKER CACHE</button>
        <div id="dev-status"></div>
    `;

    main.appendChild(panel);
    return panel;
};

const deleteAllIndexedDb = async () => {
    return new Promise((resolve, reject) => {
        if (db) {
            db.close();
            db = null;
        }
        const request = indexedDB.deleteDatabase('lists-viewer-cache');
        request.onsuccess = () => resolve();
        request.onerror = (event) => reject(event.target.error);
    });
};

const deleteAllLocalStorage = () => {
    return new Promise((resolve, reject) => {
        try {
            localStorage.clear();
            resolve();
        } catch (e) {
            reject(e);
        }
    });
};

const clearServiceWorkerCache = async () => {
    if ('serviceWorker' in navigator) {
        const registrations = await navigator.serviceWorker.getRegistrations();
        for (const registration of registrations) {
            await registration.unregister();
        }
    }

    const cacheNames = await caches.keys();
    await Promise.all(cacheNames.map(name => caches.delete(name)));

    window.location.reload();
};

const setDevStatus = (message, isSuccess) => {
    const statusEl = document.getElementById('dev-status');
    if (!statusEl) return;
    statusEl.innerHTML = `<p class="font-['Cinzel'] text-sm mt-2 ${isSuccess ? 'text-green-700' : 'text-red-700'}">${escapeHtml(message)}</p>`;
};

const showDevConfirmPopup = (title, message, onConfirm) => {
    const overlay = document.createElement('div');
    overlay.id = 'dev-confirm-popup';
    overlay.className = 'popup-overlay';

    overlay.innerHTML = `
        <div class="popup-content">
            <div class="popup-header">
                <h3 class="font-['Cinzel'] text-xl text-[var(--heading)]">${escapeHtml(title)}</h3>
                <button class="popup-close" id="dev-confirm-close">&times;</button>
            </div>
            <div class="source-filter-list">
                <p class="font-['Crimson_Pro'] text-[var(--heading)] mb-4">${escapeHtml(message)}</p>
                <div style="display: flex; gap: 0.5rem; justify-content: flex-end;">
                    <button id="dev-confirm-cancel" class="px-4 py-2 bg-[#c5a059] text-white font-['Cinzel'] hover:bg-[#c5a059]/80 transition-colors">Cancel</button>
                    <button id="dev-confirm-ok" class="px-4 py-2 bg-red-700 text-white font-['Cinzel'] hover:bg-red-800 transition-colors">Confirm</button>
                </div>
            </div>
        </div>
    `;

    document.body.appendChild(overlay);

    const close = () => overlay.remove();

    overlay.addEventListener('click', (e) => {
        if (e.target.id === 'dev-confirm-popup') close();
    });

    document.getElementById('dev-confirm-close')?.addEventListener('click', close);
    document.getElementById('dev-confirm-cancel')?.addEventListener('click', close);

    document.getElementById('dev-confirm-ok')?.addEventListener('click', async () => {
        close();
        await onConfirm();
    });
};

const initDevMode = async () => {
    const hash = window.location.hash;
    if (!hash || hash.toLowerCase() !== '#dev') return;

    const panel = createDevPanel();
    if (!panel) return;

    document.getElementById('dev-delete-idb')?.addEventListener('click', async () => {
        await showDevConfirmPopup('Delete All Cached Data', 'This will completely delete the IndexedDB database. This action cannot be undone.', async () => {
            try {
                await deleteAllIndexedDb();
                setDevStatus('IndexedDB database deleted successfully.', true);
            } catch (error) {
                console.error('Failed to delete IndexedDB:', error);
                setDevStatus('Failed to delete IndexedDB: ' + error.message, false);
            }
        });
    });

    document.getElementById('dev-delete-localstorage')?.addEventListener('click', async () => {
        await showDevConfirmPopup('Clear and Delete localStorage', 'This will completely clear all localStorage data. This action cannot be undone.', async () => {
            try {
                await deleteAllLocalStorage();
                setDevStatus('localStorage cleared successfully.', true);
            } catch (error) {
                console.error('Failed to clear localStorage:', error);
                setDevStatus('Failed to clear localStorage: ' + error.message, false);
            }
        });
    });

    document.getElementById('dev-clear-sw-cache')?.addEventListener('click', async () => {
        await showDevConfirmPopup('Clear Service Worker Cache', 'This will unregister all service workers and delete all cached assets. The app will reload and fetch fresh from the server.', async () => {
            try {
                await clearServiceWorkerCache();
                setDevStatus('Service Worker cache cleared. Reloading...', true);
            } catch (error) {
                console.error('Failed to clear SW cache:', error);
                setDevStatus('Failed to clear SW cache: ' + error.message, false);
            }
        });
    });
};

const runSearch = async (searchId, query) => {
    if (searchId === 'root-list-search') {
        const disabled = getDisabledSources();
        let baseFiltered = query ? filterFiles(query) : currentFiles;

        if (searchBody && query.trim().length > 0) {
            const bodyMatches = await searchInBodies(query, currentFiles);
            const merged = new Map();
            baseFiltered.forEach(f => merged.set(f.path, f));
            bodyMatches.forEach(f => merged.set(f.path, f));
            baseFiltered = [...merged.values()];
        }

        const filteredFiles = disabled === null ? baseFiltered : baseFiltered.filter(file => {
            const source = file.source || (file.subpath ? file.subpath.split('/')[0] : '');
            return !disabled.has(source);
        });
        const listHtml = filteredFiles.map(file => {
            const prefix = file.source ? `${file.source}/` : '';
            const subpathPart = file.subpath ? `${file.subpath}/` : '';
            const filePath = `${prefix}${subpathPart}${file.name}`;
            const sourceLabel = file.source || (file.subpath ? file.subpath.split('/')[0] : '');
            return `
                <button class="folder-btn fade-in" data-path="${escapeHtml(filePath)}" data-type="file">
                    <span>${escapeHtml(getDisplayName(file.name))}${sourceLabel ? ' <span style="opacity:0.6;font-size:0.85em">(' + escapeHtml(sourceLabel) + ')</span>' : ''}</span>
                </button>
            `;
        }).join('');

        const sourceContainer = document.getElementById('source-list-container');
        const listContainer = document.getElementById('list-list-container');
        const toggle = document.getElementById('root-list-search-body-toggle');
        if (toggle) {
            toggle.classList.toggle('hidden', query.trim().length === 0);
        }
        if (sourceContainer && listContainer) {
            if (query.trim().length > 0) {
                listContainer.innerHTML = listHtml || '<p class="text-[var(--heading)] italic">No matching lists found.</p>';
                listContainer.classList.remove('hidden');
                sourceContainer.classList.add('hidden');
            } else {
                listContainer.classList.add('hidden');
                sourceContainer.classList.remove('hidden');
            }
        }
    } else if (searchId === 'list-search') {
        let filtered = query ? filterFiles(query) : currentFiles;

        if (searchBody && query.trim().length > 0) {
            const bodyMatches = await searchInBodies(query, currentFiles);
            const merged = new Map();
            filtered.forEach(f => merged.set(f.path, f));
            bodyMatches.forEach(f => merged.set(f.path, f));
            filtered = [...merged.values()];
        }

        const container = document.getElementById('list-list-container');
        if (container) {
            container.innerHTML = renderFileButtons(filtered, currentPath);
        }

        const toggle = document.getElementById('list-search-body-toggle');
        if (toggle) {
            toggle.classList.toggle('hidden', query.trim().length === 0);
        }
    }
};

const renderRandomQuote = async () => {
    const quoteEl = document.getElementById('random-quote');
    if (!quoteEl) return;

    try {
        let text = await getCachedItem(LISTS_QUOTES_CACHE_KEY);
        if (!text) {
            const response = await fetch('https://raw.githubusercontent.com/eorroe/analyzed-lists-viewer/refs/heads/main/quotes.txt?t=' + Date.now());
            if (!response.ok) throw new Error('Failed to load quotes');
            text = await response.text();
            await setCachedItem(LISTS_QUOTES_CACHE_KEY, text);
        }
        const quotes = text.split('\n\n').map(q => q.trim()).filter(q => q.length > 0);
        if (quotes.length > 0) {
            currentQuote = quotes[Math.floor(Math.random() * quotes.length)];
            const quoteHtml = escapeHtml(currentQuote).replace(/\n/g, '<br>');
            const linked = linkifyBiblicalReferences(quoteHtml);
            quoteEl.innerHTML = linked;
            quoteEl.classList.remove('hidden');
        }
    } catch (error) {
        console.error('Failed to load quotes:', error);
        quoteEl.classList.add('hidden');
    }
};

const showQuote = () => {
    const quoteEl = document.getElementById('random-quote');
    if (quoteEl && currentQuote) {
        quoteEl.classList.remove('hidden');
    }
};

const hideQuote = () => {
    const quoteEl = document.getElementById('random-quote');
    if (quoteEl) quoteEl.classList.add('hidden');
};

const init = async () => {
    try {
        db = await openCacheDb();
    } catch (error) {
        console.error('Failed to open cache database:', error);
    }

    if (elements.themeToggle) {
        elements.themeToggle.addEventListener('click', toggleTheme);
    }
    elements.mainContent.addEventListener('click', handleItemClick);
    elements.mainContent.addEventListener('click', (e) => {
        const toggleBtn = e.target.closest('.search-toggle-btn');
        if (toggleBtn) {
            e.stopPropagation();
            searchBody = !searchBody;
            toggleBtn.textContent = searchBody ? 'Searching Titles + Body' : 'Searching Titles Only';
            const searchId = toggleBtn.dataset.searchId;
            const searchInput = document.getElementById(searchId);
            if (searchInput && searchInput.value.trim().length > 0) {
                const query = searchInput.value;
                if (searchId === 'root-list-search') {
                    rootListSearch = query;
                }
                runSearch(searchId, query);
            }
            return;
        }

        const checkBtn = e.target.closest('#check-new-source-btn, #check-new-lists-btn');
        if (checkBtn) {
            e.stopPropagation();
            if (checkBtn.id === 'check-new-source-btn') {
                handleCheckNewSource();
            } else if (checkBtn.id === 'check-new-lists-btn') {
                handleCheckNewLists();
            }
            return;
        }

        const filterBtn = e.target.closest('#filter-sources-btn');
        if (filterBtn) {
            e.stopPropagation();
            openFilterPopup();
        }
    });
    elements.retryBtn.addEventListener('click', handleRetry);
    elements.breadcrumbHome.addEventListener('click', handleHomeClick);
    elements.breadcrumbSource.addEventListener('click', handleSourceClick);

    document.getElementById('close-filter-popup')?.addEventListener('click', closeFilterPopup);
    document.getElementById('source-filter-popup')?.addEventListener('click', (e) => {
        if (e.target.id === 'source-filter-popup') {
            closeFilterPopup();
        } else if (e.target.id === 'enable-all-btn') {
            enableAllSources();
        } else if (e.target.id === 'disable-all-btn') {
            disableAllSources();
        }
    });
    document.getElementById('source-filter-list')?.addEventListener('change', (e) => {
        const input = e.target.closest('input[data-source]');
        if (input) {
            handleFilterToggle(input.dataset.source, input.checked);
        }
    });

    elements.mainContent.addEventListener('input', debounce(async (e) => {
        if (e.target.id === 'root-list-search') {
            rootListSearch = e.target.value;
            await runSearch('root-list-search', rootListSearch || '');
        } else if (e.target.id === 'list-search') {
            await runSearch('list-search', e.target.value);
        }
    }, 300));

    renderRandomQuote();

    initTheme();
    initDevMode();

    loadRootDirectories();
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => init().catch(console.error));
} else {
    init().catch(console.error);
}