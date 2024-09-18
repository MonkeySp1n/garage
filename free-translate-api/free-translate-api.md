# free-translate-api
[Papago's unofficial api](https://papago.naver.com/)
``` python
import requests
url = 'https://playentry.org/api/expansionBlock/papago/translate/n2mt'
data = requests.get(url, params={'text': TEXT, 'target': TARGET_LANGUAGE, 'source': SOURCE_LANGUAGE}).json()
# Language detection = auto
# TARGET_LANGUAGE and SOURCE_LANGUAGE must not be the same.
# Language codes use ISO 639-1.

translated_text = data['translatedText']
```
