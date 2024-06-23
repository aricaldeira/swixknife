use strict';
const CACHE_NAME = 'sezimal_pwa';

const FILES_TO_CACHE = [
    '/',
    '/long-now',
    '/now',
    '/calculator',
    '/static/css/font-iosevka.css',
    '/static/css/font-andika.css',
    '/static/css/font-noto.css',
    '/static/favicon.css',
];

self.addEventListener('install', function (evt) {
  // console.log('[ServiceWorker] Install');
  evt.waitUntil(
   caches.open(CACHE_NAME).then(function (cache) {
       // console.log('[ServiceWorker] Pre-caching offline page');
       return cache.addAll(FILES_TO_CACHE);
   })
  );
  self.skipWaiting();
});

self.addEventListener('activate', function(evt) {
  // console.log('[ServiceWorker] Activate');
   evt.waitUntil(
       caches.keys().then(function(keyList) {
           return Promise.all(keyList.map(function(key) {
               if (key !== CACHE_NAME) {
                   // console.log('[ServiceWorker] Removing old cache', key);
                   return caches.delete(key);
               }
           }));
       })
   );
  self.clients.claim();
});

self.addEventListener('fetch', function(evt) {
  if (evt.request.cache === 'only-if-cached' && evt.request.mode !== 'same-origin') {
    return;
  }
  // console.log('[ServiceWorker] Fetch', evt.request.url);
   evt.respondWith(
       caches.open(CACHE_NAME).then(function(cache) {
           return cache.match(evt.request)
               .then(function(response) {
                   return response || fetch(evt.request);
                });
       })
   );
});
