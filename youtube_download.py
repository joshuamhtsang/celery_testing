from celery import Celery
import subprocess

app = Celery(
    'youtube_download',
    backend='rpc://',
    broker='amqp://guest:guest@rabbitmq:5672'
    )


@app.task
def download_yt_video(video_id, output_filename):
    cmd = "youtube-dl -o %s -f best %s" % (output_filename, str(video_id))
    print(cmd)
    try:
        p = subprocess.Popen(
            cmd.split(" "),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        (output, stderr) = p.communicate()
        print(output)
        if p.returncode != 0:
            raise RuntimeError(stderr)
    except Exception as e:
        " !!!ERROR!!! Error when downloading video from YouTube using youtube-dl."
        print(e)
        raise e
