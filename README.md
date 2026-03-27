# coot0_9_to_1
transition from coot 0.9.x to coot 1.x
way 1. run coot 0.9.x (arm Linux) on macOS
      1.1 fully support coot 0.9 scripts
way 2. use compatible layer to run old python codes for coot 0.9.x in coot 1.x on macOS
      2.1 you only need to change `print xx` to `print()` once you load compatible layer first.
      2.2 we need to make effort together to wrap more function in compat/uf_compat_0_9.py or wait original author to release compatible layer.
