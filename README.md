# webdork
<img src="https://img.shields.io/badge/version-0.0.1-green.svg" alt="version"/>
webdork is a tool for find website vulnerability easly, This tools using google dork to find vulnerability so i think you familiar with google dork query.
this tools can save your search result, read sensitive file like .env file and many more.
<br/>
to use this tool you can <b>clone or download as zip</b> from this repository and to start this tools first of all we must install the requirements
<pre>
pip install -r requirements.txt
</pre>
after that run webdork
<pre>
py main.py
</pre>
<table>
  <thead>
    <tr>
      <th>No</th>
      <th>Command</th>
      <th>Parameter</th>
      <th>Desctrption</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td>1</td>
    <td>search</td>
    <td>keyword</td>
    <td>search the url for example i want .env file the keyword will look like this 
    <pre>
    search filetype:env intext:APP_NAME
    </pre>
    </td>
  </tr>
  <tr>
    <td>2</td>
    <td>readfile-url</td>
    <td>number index of url that showed after you search</td>
    <td>read file from the internet and save it to local directory</td>
  </tr>
  <tr>
    <td>3</td>
    <td>list-file</td>
    <td>No Parameter</td>
    <td>show files that have been read before</td>
  </tr>
  <tr>
    <td>4</td>
    <td>readfile-local</td>
    <td>No Parameter</td>
    <td>Read file that have been read before and to see history search result</td>
  </tr>
  
  </tbody>
</table>

<h1>EXAMPLE</h1>

<h4>search</h4>
in this example i looking for log files that contain the word username
<pre>
search intext:username filetype:log
</pre>

result

<pre>
You search for :  intext:username filetype:log
1 http://remikaing.free.fr/PC-DE-SARGERAN-mC:%5CUsers%5CSargeran%5CAppData%5CLocal%5CTemp%5Ctemp.log
2 http://remikaing.free.fr/HACKEURGRIS-mutXC:%5CUsers%5CYANNBA~1%5CAppData%5CLocal%5CTemp%5Ctemp.log
3 http://eplanning.sumutprov.go.id/userlevel/runtime/logs/app.log
4 https://www.picuki.com/profile/username.log
5 http://www.libre-net.nl/online/Uniserv/tcftp.log
6 https://forum.xwiki.org/uploads/short-url/ium1P63YrjUxrlAxLcOC6CrwEvz.log
7 https://justhumanz.me/ssh_fake_filter.log
8 https://www.clwk.ca/wp-content/uploads/is_iu_errors.log
9 https://jira.mariadb.org/secure/attachment/48063/slow.log
10 https://wopita.com/username.log
11 https://www.codota.com/code/java/classes/com.alibaba.druid.support.logging.Log
12 https://plaza.quickbox.io/uploads/default/original/1X/6625fea0ce4460b6212a830c1ae8aa7ceaf982f4.log
13 https://yunwei.qlecl.com/runtime/log/201903/22.log
14 http://203.151.80.164/logs/Project/UserManagement/app.log
</pre>

<h4>readfile-url</h4>

before you use this command you should search something and than you will get index number as example above, for the example i want to read
url in index 10 so the command will look loke this
<pre>
readfile-url 10
</pre>

<h4>readfile-local</h4>
readfile-local doens't require any parameter just type it. after that webdork will showing you the data and you just passing the number index of files, example
<pre>
+----+-----------+------------------------------------------------------+
| No |   Folder  |                         File                         |
+----+-----------+------------------------------------------------------+
| 1  | 10-7-2020 | fpx.mais.gov.my-af9d216201e2ead26a50aeb08de48f65.txt |
| 2  |  history  |                      result.txt                      |
+----+-----------+------------------------------------------------------+

index file > 2
</pre>
