// Step 1: get a list of all issues
// To be used on https://library.duke.edu/digitalcollections/dukechronicle/Date/
// for gathering a complete list of issues

// this is to ensure that the total count matches. You can ignore this block
all = document.querySelectorAll('p>span.facetCount')
totArticles = 0
for (i of all) {
  txt = i.innerText;
  num = /\((\d+)/.exec(txt)[1];
  totArticles += Number(num)
}

// get a dictionary file record. I chose dictionary since it's easier for import
// and it makes future processing easier.
data = {}
all = document.querySelectorAll('ul>li.termGroup.auto-truncate')
for (i of all) {
  ael = i.querySelector('a')
  des = i.querySelector('span')
  key = /dukechronicle_dchnp(\d{5})/.exec(ael.href)[1]
  data[key] = {
    date: ael.innerText,
    title: des && des.innerText
  }
}
navigator.clipboard.writeText(JSON.stringify(data))
// after this, just open fileList.json and paste 