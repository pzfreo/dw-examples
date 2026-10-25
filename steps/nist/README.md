# NIST STEP files

These are test parts from the
[NIST MBE PMI Validation and Conformance Testing Project](https://www.nist.gov/el/systems-integration-division-73400/mbe-pmi-validation-and-conformance-testing-project),
ASME variant 1, in AP242 (geometry with semantic and graphical PMI).

The five `nist_ctc_0*_asme1_ap242.stp` files (CTC-01 … CTC-05) were added first and keep
their original names. The FTC and STC files below come from `NIST-PMI-STEP-Files.zip` in
NIST's [STEP File Analyzer and Viewer](https://github.com/usnistgov/SFA) repository, commit
[`0e8d700`](https://github.com/usnistgov/SFA/tree/0e8d700ebb73db281c33441d534fe85806d5b6e7)
(2026-02-18); the name gives the AP242 edition (`-e2` is edition 2).

| File | Part | SHA-256 |
| --- | --- | --- |
| `nist_ftc_06_asme1_ap242-e2.stp` | FTC-06 | `b87afb7f25adc0d44d12e182209d50f0b085b533c0742fb8ffd58f4c87403447` |
| `nist_ftc_07_asme1_ap242-e2.stp` | FTC-07 | `aa8115c12e12a99cc439477cbfd222916f9ec629fbb3c9002b18e0c264c9a892` |
| `nist_ftc_08_asme1_ap242-e2.stp` | FTC-08 | `7b9283b4288d152fd181d76c39285d7c79fbba34fda1e14a41ac4a983f6d68b3` |
| `nist_ftc_10_asme1_ap242-e2.stp` | FTC-10 | `9d7711f48e81831c5d1838fdac5c11c0de1aa9b61f3c1d67930a7638b3b25e69` |
| `nist_ftc_11_asme1_ap242-e3.stp` | FTC-11 | `2d05bd399463a9ced7b84a479872a759f170fe92f7a62f8194e83df77f86f117` |
| `nist_stc_06_asme1_ap242-e3.stp` | STC-06 | `71777c28da76da0e8a667e4cbe792d5f72c09b5c56440c9744d3d50ca96ecc8d` |
| `nist_stc_07_asme1_ap242-e3.stp` | STC-07 | `2dddf9b8894bc241f7ffddf3dc4502baa3d49c374e8784039d14b86473d54832` |
| `nist_stc_08_asme1_ap242-e3.stp` | STC-08 | `64f24b914910ce8e20c9e4bd59637b4fd155715c7c7b51689466534ed7db1442` |
| `nist_stc_09_asme1_ap242-e4.stp` | STC-09 | `41026b1f0d81830c6092b5147e0e084d2fa163169161c31af4ce06493d3c7d33` |
| `nist_stc_10_asme1_ap242-e2.stp` | STC-10 | `fba4f46cab1ce1402362038036884631b4a41afe1c9efc5681d358c39db7ed5f` |

They are works of the U.S. federal government and are not subject to copyright in the
United States. They are vendored here unmodified so drawing builds are reproducible
without a network fetch. NIST notes that they are not reference files without errors:
conformance checkers report some syntax errors in them.
