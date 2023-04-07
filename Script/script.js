Interceptor.attach(Module.findExportByName(null, "getaddrinfo"), {
    onEnter(args) {
        args[0].writeUtf8String("127.0.0.1");
        }
    }
);