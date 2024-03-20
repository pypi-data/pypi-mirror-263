import pysrt

captions = pysrt.open('pinball_wizard-.srt')
chunkMinutes = 1
index = 0
while (captionsSection := captions.slice(
        starts_after={
            'minutes': (start := chunkMinutes * index)},
        ends_before={'minutes': start + chunkMinutes})):
    index += 1
    print(index)
    print(' '.join(captionsSection.text.splitlines()))
