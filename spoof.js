(function () {
  const spoof = {
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    screen: { width: 1920, height: 1080 },
    window: { innerWidth: 1920, innerHeight: 1000 },
    platform: "Win32",
    languages: ["en-US", "en"],
    timezone: "America/New_York",
    hardwareConcurrency: 8,
    deviceMemory: 8,
    maxTouchPoints: 0,
    webglVendor: "NVIDIA Corporation",
    webglRenderer: "NVIDIA GeForce GTX 1660 Ti / PCIe / SSE2"
  };

  function overrideProperty(obj, prop, value) {
    Object.defineProperty(obj, prop, { get: () => value, configurable: true });
  }

  // Screen & Window
  overrideProperty(screen, 'width', spoof.screen.width);
  overrideProperty(screen, 'height', spoof.screen.height);
  overrideProperty(window, 'innerWidth', spoof.window.innerWidth);
  overrideProperty(window, 'innerHeight', spoof.window.innerHeight);

  // Navigator
  overrideProperty(navigator, 'userAgent', spoof.userAgent);
  overrideProperty(navigator, 'platform', spoof.platform);
  overrideProperty(navigator, 'languages', spoof.languages);
  overrideProperty(navigator, 'language', spoof.languages[0]);
  overrideProperty(navigator, 'hardwareConcurrency', spoof.hardwareConcurrency);
  overrideProperty(navigator, 'deviceMemory', spoof.deviceMemory);
  overrideProperty(navigator, 'maxTouchPoints', spoof.maxTouchPoints);

  // Intl Timezone
  overrideProperty(Intl.DateTimeFormat().resolvedOptions(), 'timeZone', spoof.timezone);

  // WebGL
  const getParameter = WebGLRenderingContext.prototype.getParameter;
  WebGLRenderingContext.prototype.getParameter = function (param) {
    if (param === 37445) return spoof.webglVendor;     // UNMASKED_VENDOR_WEBGL
    if (param === 37446) return spoof.webglRenderer;   // UNMASKED_RENDERER_WEBGL
    return getParameter.call(this, param);
  };

  // Canvas Fingerprint Randomization
  const toDataURL = HTMLCanvasElement.prototype.toDataURL;
  HTMLCanvasElement.prototype.toDataURL = function () {
    const context = this.getContext("2d");
    context.fillStyle = "#f00";
    context.fillRect(0, 0, 1, 1);
    return toDataURL.apply(this, arguments);
  };

})();
