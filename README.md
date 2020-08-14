# lmnToDot
[LMNtal メタインタプリタ (McLMNtal)](https://github.com/lmntal/McLMNtal) の状態空間構築プログラムの出力を、 Graphviz による描画に対応した DOT 言語に変換するスクリプトです。

## Requirements
- python 3.x

## Usage
標準入力に SLIM の出力を渡すことができます。

```slim --hl --use-buiiltin-rule state_space_construction.lmn | python3 lmnToDot.py```

実行時引数にファイルを指定することもできます。

```python3 lmnToDot.py state_space.out```

以下のようなコマンドで、SLIM での LMNtal プログラム実行 → DOT 言語生成 → Graphviz による描画を一度に行うことができます。

```slim --hl --use-builtin-rule state_space_construction.lmn | python3 lmnToDot.py | dot -T png -o state_space.png```

## Options
- colored
  - ノードに着色するか選択できます