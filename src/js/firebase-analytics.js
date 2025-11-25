// Firebase Analytics configuration
// Replace these values with your actual Firebase project configuration
const firebaseConfig = {
    apiKey: "AIzaSyA3bYqcrFsRh44h6b5Vy2ggaNJH-LxTwu4",
    authDomain: "dreamflow-docs-2c50c.firebaseapp.com",
    projectId: "dreamflow-docs-2c50c",
    storageBucket: "dreamflow-docs-2c50c.firebasestorage.app",
    messagingSenderId: "426377507105",
    appId: "1:426377507105:web:7e6356038b1ca17b73ce60",
    measurementId: "G-XJVXWZ37RP"
};

// Initialize Firebase Analytics
  // Only run in the browser and in production
  if (typeof window === 'undefined' || process.env.NODE_ENV !== 'production') {
    // In dev / during SSR, do nothing
    // (avoids breaking local Docusaurus)
    // You don't need any exports here; it's just a side-effect module.
    console.info('Firebase Analytics disabled in dev/SSR.');
  } else{
  // Load Firebase SDKs dynamically using script tags (compatible with Docusaurus)
  const loadFirebaseScript = (src) => {
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = src;
      script.onload = resolve;
      script.onerror = reject;
      document.head.appendChild(script);
    });
  };

  // Load Firebase scripts and initialize
  const initializeFirebase = async () => {
    try {
      // Load Firebase SDKs
      await loadFirebaseScript('https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js');
      await loadFirebaseScript('https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js');
      
      // Wait a bit for the scripts to be available
      await new Promise(resolve => setTimeout(resolve, 100));
      
      // Initialize Firebase using the global firebase object
      const app = firebase.initializeApp(firebaseConfig);
      const analytics = firebase.analytics();
      
      // Log page views
      analytics.logEvent('page_view', {
        page_title: document.title,
        page_location: window.location.href
      });
      
      console.log('Firebase Analytics initialized successfully');
      
      // Make analytics available globally for custom events
      window.firebaseAnalytics = analytics;
      window.firebaseLogEvent = analytics.logEvent.bind(analytics);
      
    } catch (error) {
      console.error('Error initializing Firebase Analytics:', error);
    }
  };

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeFirebase);
  } else {
    initializeFirebase();
  }
}
