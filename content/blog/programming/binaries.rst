Binary Files
===============

:date: 2017-06-29
:summary: Working with binary files on Linux

Determine ARM Type
--------------------

Determine type of binary, in this case, ARMv6:

.. code-block:: bash

  pi@starfire ~ $ readelf -A /usr/local/lib/python2.7/dist-packages/cv2.so 
  Attribute Section: aeabi
  File Attributes
    Tag_CPU_name: "6"
    Tag_CPU_arch: v6
    Tag_ARM_ISA_use: Yes
    Tag_THUMB_ISA_use: Thumb-1
    Tag_FP_arch: VFPv2
    Tag_ABI_PCS_wchar_t: 4
    Tag_ABI_FP_denormal: Needed
    Tag_ABI_FP_exceptions: Needed
    Tag_ABI_FP_number_model: IEEE 754
    Tag_ABI_align_needed: 8-byte
    Tag_ABI_align_preserved: 8-byte, except leaf SP
    Tag_ABI_enum_size: int
    Tag_ABI_HardFP_use: SP and DP
    Tag_ABI_VFP_args: VFP registers
    Tag_CPU_unaligned_access: v6
    Tag_ABI_FP_16bit_format: IEEE 754

Determine needed Libraries
-----------------------------

.. code-block:: bash

    pi@fry opencv3 $ readelf -d /usr/lib/liblapack.so | grep NEEDED
     0x00000001 (NEEDED)                     Shared library: [libblas.so.3]
     0x00000001 (NEEDED)                     Shared library: [libatlas.so.3]
     0x00000001 (NEEDED)                     Shared library: [libgfortran.so.3]
     0x00000001 (NEEDED)                     Shared library: [libgcc_s.so.1]
     0x00000001 (NEEDED)                     Shared library: [libpthread.so.0]
     0x00000001 (NEEDED)                     Shared library: [libm.so.6]
     0x00000001 (NEEDED)                     Shared library: [libc.so.6]
     0x00000001 (NEEDED)                     Shared library: [ld-linux-armhf.so.3]
 
