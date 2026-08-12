# Snake, Water, Gun

A hand-game where you play against the computer, with two versions:

- **`snake_water_gun.py`** — play it in your terminal.
- **`index.html`** — play it in your browser. Instead of buttons, your
  choices sit on a triangle diagram that also shows the rule (tap a node
  to play).

**Rule:** snake drinks water, water rusts gun, gun kills snake.

## Play in the terminal

```bash
python3 snake_water_gun.py
```

Enter `s` for snake, `w` for water, or `g` for gun when prompted.

## Play in the browser

Open `index.html` in any browser — no build step or server required. Tap
one of the three nodes on the triangle to make your pick; wins, losses,
and draws are tracked below the diagram.

## Hosting the web version on GitHub Pages

1. Push this repo to GitHub (steps below).
2. On the repo page, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to `Deploy from a branch`,
   pick the `main` branch and `/ (root)` folder, then **Save**.
4. After a minute or two, your page will be live at
   `https://<your-username>.github.io/<repo-name>/`.

## Pushing this project to GitHub

From inside this folder:

```bash
git init
git add .
git commit -m "Initial commit: snake water gun (CLI + web)"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

Create the empty repo on GitHub first (no README/license, so it stays
empty) so the `git push` above has somewhere to land.
