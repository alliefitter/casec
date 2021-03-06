# `casec`

This tool was made to fix the problem of converting variable or field names from one
type of casing to another, for instance from camel case to snake case or from pascal
case to kebab case. There are often times when consuming data from an API or database
which require converting field names to another case in order to adhere to a style guide.
This can become very tedious very quickly. A regular expression may be able to solve the
problem once, but this will only convert one case to another. You would need several
regular expressions for each conversion if you were to want to handle multiple naming
conventions. `casec` makes all of this much easier. 

Converting one naming convention to another reduces to two basic problems. Parsing a 
delimited string into words and formatting words into a delimited string. The delimiter
in this case can either be a character, such as an underscore or dash, or the case of
a character.
   
There is also some nuance in naming conventions that is difficult to account for
with regular expressions, especially concerning camel case and pascal case. How should 
acronyms be handled? Should a camel cased name have "VPN" formatted in all caps or as "Vpn"? 
What of proper nouns with a standard casing such as "iOS"? Should it be formatted as "IOs"
in pascal case? When converting a camel cased name, "iOSUsername," to snake case, how should
"iOS" be parsed? Should the result be "ios_username" or "i_os_username"? The answers to these
questions can vary based on the style guide you're using. One the goals of `casec` is  to
handle situations like these dynamically in straightforward way. 


## Installation

```
$ pip install casec
```

## Usage

Basic usage is as simple as `casec snake-case -c -f <file name>`. This converts a file of
snake cased names to camel-case.

```bash
$ cat some_snake_cased_names
login
id
node_id
avatar_url
gravatar_id
url
html_url
$ casec snake-case -c -f some_camel_cased_names
login
id
nodeId
avatarUrl
gravatarId
url
htmlUrl
```

Other cases are just as simple.

```bash
$ cat some_pascal_cased_names
Login
Id
NodeId
AvatarUrl
GravatarId
Url
HtmlUrl
$ casec pascal-case -c -f some_pascal_cased_names
login
id
nodeId
avatarUrl
gravatarId
url
htmlUrl
$ casec pascal-case -s -f some_pascal_cased_names
login
id
node_id
avatar_url
gravatar_id
url
html_url
$ casec pascal-case -k -f some_pascal_cased_names
login
id
node-id
avatar-url
gravatar-id
url
html-url
```

Stdout may be piped into as well.

```bash
$ cat some_kebab_cased_names
login
id
node-id
avatar-url
gravatar-id
url
html-url
$ cat some_kebab_cased_names | casec kebab-case -c
login
id
nodeId
avatarUrl
gravatarId
url
htmlUrl
$ cat some_kebab_cased_names | casec kebab-case -c | casec camel-case -s
login
id
node_id
avatar_url
gravatar_id
url
html_url
```

As mentioned above, case sensitive string literals may be provided to assist in parsing or 
formatting names. When parsing `camel-case` and `pascal-case`, the `-l, --literals` switch 
can be used to provide a comma separated list of literals.

```bash
$ cat some_other_camel_cased_names
iOSApp
iTunesStoreId
$ cat some_other_camel_cased_names | casec camel-case -s
i_os_app
i_tunes_store_id
$ cat some_other_camel_cased_names | casec camel-case -s -l iOS,iTunes
ios_app
itunes_store_id
```

Using the `-r, --format-literals` switch, output can be formatted.

```bash
$ cat some_other_snake_cased_names | casec camel-case -s -l iOS,iTunes
ios_app
itunes_store_id
$ cat some_other_snake_cased_names | casec camel-case -s -l iOS,iTunes
iOSApp
iTunesstoreId
$ cat some_other_snake_cased_names | casec camel-case -s -l iOS,iTunes,ID
iOSApp
iTunesstoreID
```

Field names from a JSON object can be converted to another case easily with `jq`.

```bash
$ cat some_json.json
{
  "login": "octocat",
  "id": 1,
  "node_id": "MDQ6VXNlcjE=",
  "avatar_url": "https://github.com/images/error/octocat_happy.gif",
  "gravatar_id": "",
  "url": "https://api.github.com/users/octocat",
  "html_url": "https://github.com/octocat",
  "followers_url": "https://api.github.com/users/octocat/followers",
  "following_url": "https://api.github.com/users/octocat/following{/other_user}",
  "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
  "organizations_url": "https://api.github.com/users/octocat/orgs",
  "repos_url": "https://api.github.com/users/octocat/repos",
  "events_url": "https://api.github.com/users/octocat/events{/privacy}",
  "received_events_url": "https://api.github.com/users/octocat/received_events",
  "type": "User",
  "site_admin": false
}
$ cat some_json.json | jq -r 'keys[]' | casec snake-case -c
avatarUrl
eventsUrl
followersUrl
followingUrl
gistsUrl
gravatarId
htmlUrl
id
login
nodeId
organizationsUrl
receivedEventsUrl
reposUrl
siteAdmin
starredUrl
subscriptionsUrl
type
url
```

There's other 
