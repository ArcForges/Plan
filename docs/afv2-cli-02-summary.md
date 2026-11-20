# AFV2-CLI-02 native terminal evidence

Node PR 110 merged at `402ddf9a83478eeddb29b049daa940b7151bab0d`. Its file
tree matches reviewed head `41a9e1b7c1324bde7c80ab39ee6e8d36ffe4e6f9`
and tree `4bdd731affca4b25c35ca97a1f360f0ec038f937`. The independent
source review checked all 22 changed paths against the scope in Plan PR 203.
The preceding author head `e1c31a18d7c82641a0bf02f02ec6dc25f885d0a7` passed
all 10 focused installed CLI cases with zero skips on each native host.
The final change rechecks the same observation after the native test
reader finishes draining.

Both exact GitHub verifier statuses were successful before the merge.
The Node main push showed no publication workflow.

AFV2-CLI-02 uses the qualified official MXC 1.0.1 profiles on both hosts. The CLI connects the caller's native terminal to the original supervisor-owned PTY or ConPTY. Default foreground Start prints its original Run, command and owner epoch before attaching. A detached Start still returns its receipt. An attachment can observe output, own the writer lease or explicitly take over. A local detach releases the exact original lease and leaves the Run under Node management. Linux holds its raw input lease on the actual TTY, and Windows serializes competing caller console mutations. The tests exercise independent consoles and reject the second mode-changing CLI on the same one.

The two fixed official inner ConPTY messages ESC[?9001h and ESC[?9001l are consumed only by the local Windows renderer. The Windows input adapter continues to receive normal keyboard characters in the qualified fixture. Original retained bytes and byte-exact redirected output remain available. The host adapter can cancel blocked native output on the tested ConPTY. If a completely unread consumer prevents verified mode restoration, the adapter reports the uncertainty. A separate diagnostic resumed the consumer and measured restoration of the original input and output mode flags.

Native tests exercise a full-screen TUI, both terminal sizes and redraw, UTF-8, Ctrl+C, detach and same-owner reattach, cooked interruption, exact binary pipes and explicit stdin EOF. A saved live typed offset returns the byte-exact settled suffix, and the separate complete output check includes every retained byte. GAP is reported on stderr and in the selected JSON stream. Output from a live non-follow read uses a bounded receive window and reports its next offset on stderr when no final state was observed.

The genuine pipe pressure fixture lost an input acknowledgment while the native reader was held. The original CLI identified the unknown effect and required explicit attachment. The stored observation is a tested prefix from the native reader, and additional possible earlier effect remains unknown. A new lease started at sequence zero and the independent Stop proved the Run group empty. Other native cases verify prior acknowledged input, Node restart, the expired writer/acknowledgment window and a fresh writer without replay. The quiet fixture scans durable state and separately checks retained program output. The CLI only advances the accepted suffix of a confirmed native frame. Any uncertain mutation stops automatic forwarding.

The fixed profiles report the observed official executor code and verify the native boundary is empty in the accepted cases. Their native exit records leave payload startup unconfirmed. The CLI propagates a representable nonzero executor code and identifies its provenance. An observed executor zero with unknown payload startup returns 8. Independent native fixture markers record the application effects used to qualify terminal behavior, without substituting those markers for the product's trusted startup field.

## Verified installation evidence

Both final-head installed suites passed 42/42 with zero skips. They used a
fresh verified extraction of the native archive, the pinned official MXC
assets and the Native AOT TestLoad for that host. Each reporter fetched the
same GitHub PR head independently. Raw reports stay under the Node
repository's `.git/arcforges-verify/` directory on each designated host.

| Focused author receipt at e1c31a1 | Cases | Native log SHA-256 |
| --- | --- | --- |
| Windows deku | 10/10 | 4f0665267732f136916f1f39b86f221db58972f18fd4938ff3c850c87ea6755d |
| Linux H-22 | 10/10 | 02d8d9161a7f130eed90520e4f63393a5ccce3d160e4f02de9930a307cb6a21c |

The author runs used `--filter-class ArcForges.ClosedLoop.Tests.MxcRunServiceTests --filter-method '*InstalledCli*' --parallel none --minimum-expected-tests 10 --fail-skips on --output Detailed`.

### H-22 exact final profile

The designated Linux host passed all 20 required checks in 2660
seconds. The installed suite passed 42/42 with zero skips. The exact
final package separately passed the operator PTY sample. Its record
observed 24×80 at payload readiness, then 27×93 and 35×107. The same Run
continued after detach status 0. The reattached CLI returned 8 after the
observed official executor zero with unknown payload startup. The original
terminal attributes and fixture cleanup were verified.

| H-22 artifact | SHA-256 |
| --- | --- |
| 20261120-093908-41a9e1b7c132-linux/summary.json | db842eca3a8aad247b26c71feeea62c043e4c9265a3b7d64b34788cd08e22fc3 |
| linux-package.log | fa75f07a0da3ad91c00832c4371c5b3b23c1ddbbfca67a9424baddfb4c82ca21 |
| arcforges-linux-x64.tar.gz | 5c298e27b63cee1250519a9b9bd48d856c71061c1c2fe751f4066d00c01bfc87 |
| Official MXC stage manifest | f5332ecb0bc91338a2d0e2ed8ae7b797d028d1743051270b24b404beef820a2d |
| linux-manual-41a9e1b7c132-operator/console.bin | 5c9ba522e33c0ad9a9d0c5580830c4e69651351dc0c631fe1acdf88585c3f3c6 |
| linux-manual-41a9e1b7c132-operator/finish.json | ed1f7494aea3d76d1b032e942691dc36dbeb57272d1bd9ceef976715a499cd43 |
| Operator terminal-marker.log | ead5db3fc239854df4e9986ce48ce12a2dbd8fc058ea34db5ce798947c2360d8 |
| Operator run-final.json | a36502890eceb11761455c44caf46ae52f4e1b0da9baab13d65fc6878188c287 |
| Isolated Node Stop | b36d178acad9acba3efe5868d8557f71842641478391f3ce6a224c06275269fb |

The private operator marker and JSON receipts are in
`/home/sammiller/arcforges/cli02-manual-linux.YhjdIPgK/receipt/`. The
controller transcript and completion record are in the Node
repository's `.git/arcforges-verify/launches/cli02-intake/`.

### Windows exact final profile

The Windows workstation passed all 15 required checks in 3080 seconds.
The installed suite passed 42/42 with zero skips. A separate operator
sample on the exact installed package verified 27×93 and 35×107, Unicode
and raw Ctrl+C. Default detach returned 0 and the same Run epoch remained
RUNNING. A fresh lease reattached to it. The caller's input and output
mode flags returned to 503 and 7 after detach and after reattached exit.
The official executor zero with unknown payload startup produced CLI
status 8, and both the Run boundary and isolated Node stopped.

| Windows artifact | SHA-256 |
| --- | --- |
| 20261120-093908-41a9e1b7c132-win/summary.json | 6bac9678c6bd5bfcef176b9888a56622d8256c505b5e771a132c96f1c7063eed |
| win-package.log | 4be16b0f5303c630c225ad8706905e419d1a1859fdbef2cced0b49d41ac1e0a1 |
| arcforges-win-x64.zip | 9facf30aa31c0fe3cc084a6287fc411f6194674a4beb67499a2fd00e56de01f5 |
| Official MXC stage manifest | 826c78d253a9ea35af5d871c48c50590b9dec011d2bb07ee8963592b22fd8817 |
| win-manual-41a9e1b7c132/console.bin | 08506317fe042e4f817f01dae6ccd90f99f361a8bc57597211412ec3fc942b03 |
| win-manual-41a9e1b7c132/finish.json | d31e9b674c055b132ab26e34e35d497df7c6c93ca8a0cf5537f56d982ed7aaac |
| Operator run-final.json | e88b6ff8e796da5a813115babd7a63a3b2d6f81d482de11872a794d35169dfce |
| Isolated Node Stop | 22c757f523edd4818173e3d69730aa8c0e4d22d1e36c9bb5ca19c2b5ff3dd7e9 |

The private operator JSON receipts are in the workstation's
`LocalAppData/Temp/arcforges-cli02-manual-6b91798640d1/receipt/`.
The controller transcript and completion record are in the Node
repository's `.git/arcforges-verify/launches/cli02-intake/`.

## Preserved negative and diagnostic evidence

| Head and host | Observed result | Native log SHA-256 |
| --- | --- | --- |
| 7e614415 Windows first launch | AOT emitted a localized warning summary that the stock publisher could not parse. The repeat selected the repository's English build-output environment. | 62f579ac63fe4fe365a57bc888be482dbe57e7a01b5c4f928ceb646def022f19 |
| 7e614415 Windows repeat | 7/10. The readiness gates assumed the caller geometry before attachment had resized the payload. The Windows CMD stderr fixture emitted a trailing space, which the CLI preserved. | ebc1587018f3a390741682cdf2803bf801babf38a6694f72eabb2764292df2dc |
| 7e614415 H-22 | 8/10. The two startup probes required a particular readiness marker before the native Resize. | d5a37907fb999a09d13c831b8083c09117c100becfdb2b0d6afa3a70377c65a3 |
| d5c36f3 H-22 | 9/10. The takeover fixture read the supervisor row while the Run could still be STARTING. | c038190d0ee0b95b69420cdcbcda21f9d65f333105e8a8c1c5cb91733fda38b8 |
| 4a0032e Windows | 8/10. The same early owner lookup failed. Default detach also reached the actual application under the nested Win32 keyboard mode. | ebea541c4a9bbed35028fdf3d0ef7f93516515e7087aa4d0e05d3806b47b18b2 |
| 2a895a4 H-22 | 9/10. A new EOF after an earlier lost write acknowledgment also returned UNKNOWN. The fixture now observes the original native prefix and uses a separate verified Stop after acquiring the fresh lease. | b863ed8d9e008d6b7ba02d56caa79a5092c2e8e5b30e210b50ff8768f8176511 |
| 124d98b Windows | 9/10. Local detach and a later native Resize passed. A repeated size string in rendered output could not identify byte replay at the saved cursor. The repeat verifies the exact retained suffix. | 17191c570f593674840e10302ac14eb0ee8a03ba2355706cf9c78dcd0370f1f4 |
| 124d98b H-22 | 9/10. The CLI returned 8 after application quit. The fixture did not capture its expected executor provenance diagnostic and the original log does not establish the reason. The repeat keeps the actual TUI alive past the quit write, verifies another native resize on the same mutation lane and rechecks the fully drained console. | 04bd461001e2f4cb19af79dc3d752acaf600d08ed3bea0596ab40952e45977ed |

A Windows manual run of 4a0032e reproduced forwarding of the default
detach key to the real application. The separate private diagnostic built
a traced Native AOT CLI with the original official runtime assets in a
private extraction. It confirmed that the input adapter received native
Win32 keyboard envelopes after the standalone inner negotiation.
The Windows raw console SHA-256 is
`46d408a15ac9f65f2ce579f8d2d16b38cfeb5eb17e987d4bc9d3d63f78b643be`.
The private synthetic input diagnostic SHA-256 is
`fae580034f5b9ae0224880ab13910eedc5fac8d86c340d5228bb5b8399f9faf2`.

The corrected production source at 124d98b passed independent operator
samples on both hosts. The samples exercised an actual separate ConPTY
or controlling PTY with Unicode, resize, interruption input, detach and
same-Run reattach, caller mode restoration and verified Run and isolated
Node cleanup. Their raw console SHA-256 digests are
`f499d05dde3b0ef0b7cd401ae2682cb965cd52c8b932d4d27d6bbe6d67f7d8e8` for Windows and
`d608ceac575e3da068cbf1bbb18d90afcd08666c3786cceb6cc1b87cff5eb7dc` for H-22.

See [Node PR 110](https://github.com/ArcForges/ArcForges/pull/110),
[Plan PR 202](https://github.com/ArcForges/Plan/pull/202) and
[Plan PR 203](https://github.com/ArcForges/Plan/pull/203).
