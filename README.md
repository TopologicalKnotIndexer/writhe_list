# Writhe list

Diagram writhe values for the 1,783 PD-code representatives in the
TopologicalKnotIndexer composite-knot catalog.

## Data format

`data/writhe_list.txt` contains records of the form:

```text
[WRITHE|PD_CODE|KNOT_NAME]
```

The file has 1,783 lines and includes the unknot, prime knots, mirrors, and
composites. Writhe is a property of an oriented diagram rather than an ambient
isotopy invariant by itself; values are tied to the exact PD representatives
stored alongside them.

## Regeneration

The repository includes its complete input baseline at
`data/com_pd_code_list.txt`, so regeneration does not depend on another clone.
With SageMath available, run:

```bash
sage -python data/calc.py
```

The generator parses PD literals without `eval()`, computes `Knot(pd).writhe()`,
and always writes `data/writhe_list.txt` relative to the script.

## Consuming the data

Because a PD code may contain many `|`-free list tokens, split each record with
`line[1:-1].split("|", 2)` to obtain writhe, code, and name.

## License

MIT. See `LICENSE`.

## Citation

If you use this repository in academic work, please cite it as:

```bibtex
@software{topologicalknotindexer_writhe_list,
  author = {{TopologicalKnotIndexer contributors}},
  title = {{writhe\_list}},
  year = {2026},
  url = {https://github.com/TopologicalKnotIndexer/writhe_list}
}
```
