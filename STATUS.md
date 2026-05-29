# Top Huatulco status — 2026-05-28

Working folder: /home/osohermes/projects/top-huatulco
Live preview alias: https://top-huatulco.vercel.app
GitHub backup: https://github.com/mgallard/top-huatulco
Latest commit: e4479c3 Build Top Huatulco tourism site structure
Vercel project: top-huatulco under mogensgallardo-8987s-projects; preview/staging alias only, no TopHuatulco.com DNS connected.

Current state:
- Rebuilt as a 46-route Vite/Tailwind static tourism guide based on Top El Salvador structure.
- Routes include homepage, nine-bay destination hub + all 9 bay pages, beaches, towns, things-to-do, tours, food, 4 itineraries, 7 travel-guide pages, about/privacy/terms/image-credits, robots.txt, and sitemap.xml.
- Verification passed: npm run test, npm run lint, npm run build; remote marker checks passed on representative live routes; browser visual QA passed homepage and bays hub.

Known blockers / next actions:
1. Kanban DB currently errors with `no such column: claim_lock`, so card creation/update failed. A DB backup was made before attempted repair. Use COMMAND_CENTER.md as fallback until Kanban is repaired.
2. Real Huatulco media pass needed. Current hero/media are carried over from scaffold and not launch-quality.
3. Source-freshness and local directory depth pass needed before production DNS: official/current links, named restaurants/operators/hotels, route-specific photos, and richer priority pages.

Resume command:
cd /home/osohermes/projects/top-huatulco && hermes --resume
