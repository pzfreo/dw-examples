# text-to-cad STEP files

These parts come from [text-to-cad](https://github.com/earthtojake/text-to-cad)'s example
models, as they stand on the branch of
[earthtojake/text-to-cad#674](https://github.com/earthtojake/text-to-cad/pull/674)
(`amywork777/text-to-cad-upstream`, commit
[`85d8fdb`](https://github.com/amywork777/text-to-cad-upstream/tree/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3), 2026-10-29).

text-to-cad publishes its models as build123d Python, not as STEP files, so **these STEP files
are exports, not original files**. Each was made by calling the model function in its source
file and writing the returned shape with build123d 0.13.0's `export_step`, unchanged
otherwise. The model geometry is text-to-cad's own, including its mistakes: in the L bracket
the ⌀6 holes overlap the gussets by 2 mm.

| STEP file | Model source | SHA-256 of the export |
| --- | --- | --- |
| `angle-bracket.step` | [`models/examples/src/angle_bracket.py`](https://github.com/amywork777/text-to-cad-upstream/blob/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3/models/examples/src/angle_bracket.py) | `c056160beb6f2b6a2551b2449a2a066144f789a91e48661b536a1acb94ab2ba7` |
| `circular-flange.step` | [`models/examples/src/circular_flange.py`](https://github.com/amywork777/text-to-cad-upstream/blob/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3/models/examples/src/circular_flange.py) | `3d8898362219921afa7cf0a18b4afe9a5239070aa5c14b4387ad7767737cf392` |
| `electronics-enclosure-base.step` | [`models/examples/src/electronics_enclosure_base.py`](https://github.com/amywork777/text-to-cad-upstream/blob/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3/models/examples/src/electronics_enclosure_base.py) | `8448a2ae72a69f49076cc50ff38807874b90dd2febc9968d763a6a5816670c3e` |
| `guide-bar.step` | [`models/examples/src/guide_bar.py`](https://github.com/amywork777/text-to-cad-upstream/blob/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3/models/examples/src/guide_bar.py) | `aa1e28d6c399932dbe64682f06b77e524500e8397237d2899f3b4ac74dbed26c` |
| `l-bracket.step` | [`models/examples/src/l_bracket.py`](https://github.com/amywork777/text-to-cad-upstream/blob/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3/models/examples/src/l_bracket.py) | `8312c5a3a77427f1dc83016b529f0e929ce0776716e411b85ce58ee0918203e2` |
| `mounting-plate.step` | [`models/examples/src/mounting_plate.py`](https://github.com/amywork777/text-to-cad-upstream/blob/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3/models/examples/src/mounting_plate.py) | `1e71caba689593eb357ca6ac0108130c2655adfda280909db88f49a8baf3c750` |
| `perforated-plate.step` | [`models/examples/src/perforated_plate.py`](https://github.com/amywork777/text-to-cad-upstream/blob/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3/models/examples/src/perforated_plate.py) | `796b67866ae0eed937f322432d8d32d6996cab9f359b77f9deaf30fb7e1e5cba` |
| `pivot-mount-plate.step` | [`models/examples/src/pivot_mount_plate.py`](https://github.com/amywork777/text-to-cad-upstream/blob/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3/models/examples/src/pivot_mount_plate.py) | `181c4eb7d886b9b301a29ef4542445f91ed862057d0fc2ec97def86def21ec26` |
| `stepped-shaft-keyway.step` | [`models/examples/src/stepped_shaft_keyway.py`](https://github.com/amywork777/text-to-cad-upstream/blob/85d8fdbfb467ebd7e22994fe8bcd86afa6626ed3/models/examples/src/stepped_shaft_keyway.py) | `587c4f4eaf5f9c28a74521aac5619b6ea51c0554735cb0bdd3f583d8b7cb9f95` |

The pivot mount plate is a three-part assembly (plate, bushing, liner); draftwright draws the
plate and notes the parts it leaves out.

text-to-cad is copyright Thompson Labs LLC and licensed under the MIT License, reproduced in
[`LICENSE`](LICENSE).
