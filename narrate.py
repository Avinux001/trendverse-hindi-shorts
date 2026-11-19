import argparse, asyncio, json, subprocess
from pathlib import Path
import edge_tts

async def main():
    p=argparse.ArgumentParser()
    p.add_argument('--script', default='script.txt')
    p.add_argument('--output', default='narration.mp3')
    p.add_argument('--voice', default='hi-IN-SwaraNeural')
    a=p.parse_args()
    text=Path(a.script).read_text(encoding='utf-8').strip()
    if not text: raise SystemExit('Script is empty')
    if not a.voice.startswith('hi-IN-'): raise SystemExit('Hindi voice required')
    await edge_tts.Communicate(text, a.voice, rate='-3%').save(a.output)
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size','-of','json',a.output]))
    f=probe['format']; duration=float(f['duration']); size=int(f['size'])
    if duration<3 or size<8000: raise SystemExit(f'Audio failed QA: {duration}s {size} bytes')
    print(f'Audio generated: {a.output} ({duration:.1f}s, {size} bytes)')

if __name__=='__main__': asyncio.run(main())
