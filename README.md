# TrendVerse Hindi narration cloud workflow

A GitHub Actions workflow that runs at 10:00, 15:00, and 20:00 India time (UTC 04:30, 09:30, 14:30) or manually. It generates an MP3 artifact using Edge TTS Hindi SwaraNeural, validates duration and size, and uploads the MP3 as a downloadable workflow artifact. It does NOT create or publish a video, and does not connect itself to the ChatGPT scheduler or vidIQ.

## Deploy from an Android phone

1. Connect GitHub to ChatGPT, or create a GitHub repository using the mobile browser.
2. Add all files, preserving `.github/workflows/hindi-voice.yml` path.
3. Go to Actions > Hindi narration > Run workflow to test.
4. Open the completed run and download `hindi-narration` artifact.

## Important limits

Edge TTS is an unofficial online interface; its availability, commercial permissions, and rate limits are not guaranteed. Before commercial publishing, verify rights for the chosen voice and service. The workflow requires Internet access and can fail if the service is blocked. GitHub Actions usage is subject to free-plan allowances and scheduled jobs may be delayed. This workflow is a testable cloud bridge, not a guarantee of perpetual free speech synthesis or autonomous YouTube publishing.
