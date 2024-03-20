### dekcli

```shell
# Add site and Input a token from gitea web, then adding local ssh token to the site settings
dekcli gitea login https://sample.com

dekcli gitea init /path/to/git/dirs/tree

# Add secrets according to index.yaml

dekcli gitea push /path/to/git/dirs/tree
dekcli gitea pull /path/to/git/dirs/tree
```
