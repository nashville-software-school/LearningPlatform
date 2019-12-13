const instructorSelect = document.querySelector("#div_id_instructor select")
const studentSelect = document.querySelector("#div_id_student")
studentSelect.classList.add("hidden")

instructorSelect.addEventListener('change', function(evt)  {
  studentSelect.classList.remove("hidden")
  const instructorId = this.value;  // get the selected instructor ID from the HTML input
  const url = `${document.querySelector('form[id$="_form"]').getAttribute("data-students-url")}/${instructorId}`;  // get the url of the `load_students` view and add the instructor id to the url params

  fetch(url)
  .then(data => data.text()) //Have to use .text() to convert HTML data sent from Django's render()
  .then(studentOptions => {
    const studentSelect = document.querySelector("#id_student")
    // And now, a whole lot of crap to avoid using innerHTML. Surprisingly, this is all faster than using jQuery!
    const frag= document.createDocumentFragment()
    // Can't add our studentOptions HTML string directly tot he fragment, so we make a div, then...
    let temp = document.createElement('div')
    // ...then add the string to RTCDtlsTransportStateChangedEvent. But we don't want the div in the DOM, so...
    temp.innerHTML = studentOptions
    // ...we loop through its children, which is/are now proper DOM nodes and append to the fragment
    while(temp.firstChild) {
      frag.appendChild(temp.firstChild);
    }
    // ...then we dump the existing student choices
    while (studentSelect.firstChild) {
      studentSelect.firstChild.remove();
    }
    studentSelect.appendChild(frag)
  })
})
