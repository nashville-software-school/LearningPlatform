
// When this is selected...
const typeSelect = document.querySelector("#div_id_disengagement_type select")

// show the appropriate follow-up input
const disegDetail = document.querySelector("#div_id_disengagement_detail")
const reasonSelect = document.querySelector("#div_id_reason")
const returnDate = document.querySelector("#div_id_intended_return_date")
const returnCondition = document.querySelector("#div_id_return_conditions")
reasonSelect.classList.add('hidden')
disegDetail.classList.add('hidden')
returnDate.classList.add('hidden')
returnCondition.classList.add('hidden')

typeSelect.addEventListener('change', function(evt)  {
  if (this.value == "2") { //student is going on leave ( with specific or general plan to return )
    disegDetail.classList.remove('hidden')
    returnDate.classList.remove('hidden')
    returnCondition.classList.remove('hidden')
    if (!reasonSelect.classList.contains("hidden")) {
      reasonSelect.classList.add("hidden")
    }
  } else { // student is leaving NSS permanently
    reasonSelect.classList.remove('hidden')
    if (!disegDetail.classList.contains("hidden")) {
      disegDetail.classList.add("hidden")
      returnDate.classList.add('hidden')
      returnCondition.classList.add('hidden')
    }
  }
})
