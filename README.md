# uv-playground

Demo repo for the team presentation on `uv` and how we manage Python dependencies, using [uv-joke-lib](https://github.com/alboman8/uv-joke-lib) as the example shared library. Commands below assume you're inside this folder.

## 1. No `.venv` yet

```bash
ls -la
```

## 2. Sync the `dev` group and run

```bash
uv sync --group dev
ls -la
uv run --group dev python main.py
```

## 3. Switch to `test`

```bash
uv sync --group test
uv run --group test python main.py
```

## 4. Switch to `prod`

```bash
uv sync --group prod
uv run --group prod python main.py
```

## 5. Add and remove a dependency

```bash
uv add requests
uv sync --group dev
uv remove requests
uv sync --group dev
```

## 6. `uv sync` without a group

Only installs the base `dependencies`, none of `prod`/`test`/`dev`:

```bash
uv sync
```

## 7. `uv lock --upgrade` with no upstream changes

```bash
uv lock --upgrade
```

Nothing changes, `joke-lib` hasn't moved on the tracked refs.

## 8. Pick up a change from the `dev` branch

In [uv-joke-lib](https://github.com/alboman8/uv-joke-lib): make a change on `dev`, commit, push.

Back here:

```bash
uv run --group dev python main.py
```

Still the old output, `uv.lock` hasn't moved.

```bash
cat uv.lock | grep -A1 "name = \"joke-lib\""
uv lock --upgrade
uv run --group dev python main.py
```

Now it reflects the new commit.

```bash
uv sync --group test
uv run --group test python main.py
```

`test`/`prod` are unaffected, they're pinned to different refs (`main`/a tag).

## 9. (Bonus) Editable install for local development

If you're changing `uv-joke-lib` and `uv-playground` at the same time and don't want to push every change just to test it, clone [uv-joke-lib](https://github.com/alboman8/uv-joke-lib) as a sibling directory (`../uv-joke-lib`):

```bash
uv pip install -e ../uv-joke-lib
uv run --group dev python main.py
```

Your local, uncommitted changes to `uv-joke-lib` are picked up immediately. Running a plain `uv sync` afterward reverts back to whatever is pinned in `uv.lock`:

```bash
uv sync --group dev
```
