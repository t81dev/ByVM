void call_ffi(uint8_t func_id) {
    switch (func_id) {
        case 0x01:
            printf("Hello from C FFI!\n");
            break;
        default:
            printf("Unknown FFI function: %d\n", func_id);
    }
}

