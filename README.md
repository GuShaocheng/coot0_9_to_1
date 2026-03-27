# coot0_9_to_1

Transition from coot 0.9.x to Coot 1.x

## Options

### Way 1: Run Coot 0.9.x (ARM Linux) on macOS
- https://drive.google.com/drive/folders/1klDIpBIr76bhaoQf1kKVQrSaTAzGoRuE?usp=sharing
- Run smoothly and Fully supports coot 0.9 scripts

### Way 2: Use a compatibility layer to run old Python code (Coot 0.9.x) in Coot 1.x on macOS
- Only need to change `print xx` → `print()`
- Additional functions may need to be wrapped in `compat/uf_compat_0_9.py` to support all coot 0.9 scripts
- Contributions are welcome, or wait for the original author to release his compatibility layer
