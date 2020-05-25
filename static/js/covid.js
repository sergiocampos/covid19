function activeOutrasCardiopatias(){
	if (document.getElementById('check_outras_cardiopatias').checked == true) {
		$("#outras_cardiopatias").prop("disabled", false);
	}
	else {
		$("#outras_cardiopatias").val("");
		$("#outras_cardiopatias").prop("disabled", true);
	}
}

function activeIdadeGestacional(){
	if (document.getElementById("check_idade_gestacional").checked == true) {
		$("#idade_gestacional").prop("disabled", false);
		$("#gesta_para").prop("disabled", false);
	}
	else {
		$("#idade_gestacional").val("");
		$("#idade_gestacional").prop("disabled", true);
		$("#gesta_para").val("");
		$("#gesta_para").prop("disabled", true);
	}
}

function comorbidadesObstetrica(){
	if (document.getElementById("check_comorbidades_obstetrica").checked == true) {
		$("#comorbidades_obstetrica").prop("disabled", false);
	}
	else {
		$("#comorbidades_obstetrica").val("");
		$("#comorbidades_obstetrica").prop("disabled", true);
	}
}

function check_outro_medicamento(){
	if (document.getElementById("outros_medicamento").checked == true) {
		$("#descricao_outro_medicamento").prop("disabled", false);
	}
	else {
		$("#descricao_outro_medicamento").val("");
		$("#descricao_outro_medicamento").prop("disabled", true);
	}
}

function activeDateHeparina(){
	$("#date_inicio_heparina").prop("disabled", false);
	$("#heparina_tipo").prop("disabled", false);
	$("#heparina_dose").prop("disabled", false);
}

function desactiveDateHeparina(){
	$("#heparina_tipo").val("");
	$("#heparina_dose").val("");
	$("#date_inicio_heparina").val("");
	$("#date_inicio_heparina").prop("disabled", true);
	$("#heparina_tipo").prop("disabled", true);
	$("#heparina_dose").prop("disabled", true);

}