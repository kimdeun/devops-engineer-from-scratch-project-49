install:
	uv sync
brain-games:
	uv run brain-games
brain-even:
	uv run brain-even
brain-calc:
	uv run brain-calc
brain-gcd:
	uv run brain-gcd
brain-progression:
	uv run brain-progression
brain-prime:
	uv run brain-prime
build:
	uv build
package-install:
	uv tool install dist/*.whl
package-reinstall:
	uv tool install --force --reinstall dist/hexlet_code-0.1.0-py3-none-any.whl
lint:
	uv run ruff check brain_games
