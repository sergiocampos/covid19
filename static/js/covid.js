function activeOutrasComorbidades(){
	if (document.getElementById('outras_comorbidades').checked == true) {
		$("#desc_outras_comorbidades").prop("disabled", false);
	}
	else{
		$("#desc_outras_comorbidades").prop("disabled", true);
		$("#desc_outras_comorbidades").val("");
	}
}

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

function desactiveFoco(){
	$("#foco_pulmonar").prop("disabled", false);
	$("#foco_urinario").prop("disabled", false);
	$("#foco_pele").prop("disabled", false);
	$("#foco_abdominal").prop("disabled", false);
	$("#foco_corrente_sanguinea").prop("disabled", false);
}

function activeFoco(){
	$("#foco_pulmonar").prop("checked", false);
	$("#foco_urinario").prop("checked", false);
	$("#foco_pele").prop("checked", false);
	$("#foco_abdominal").prop("checked", false);
	$("#foco_corrente_sanguinea").prop("checked", false);

	$("#foco_pulmonar").prop("disabled", true);
	$("#foco_urinario").prop("disabled", true);
	$("#foco_pele").prop("disabled", true);
	$("#foco_abdominal").prop("disabled", true);
	$("#foco_corrente_sanguinea").prop("disabled", true);
}

function activeDataColeta(){
	$("#data_coleta").prop("disabled", false);
}

function desactiveDataColeta(){
	$("#data_coleta").val("");
	$("#data_coleta").prop("disabled", true);
}

function activeDoseCorticosteroide(){
	$("#corticosteroide_id").prop("disabled", false);
	$("#data_inicio_corticosteroide_id").prop("disabled", false);
}

function desactiveDoseCorticosteroide(){
	$("#corticosteroide_id").val("");
	$("#data_inicio_corticosteroide_id").val("");
	$("#corticosteroide_id").prop("disabled", true);
	$("#data_inicio_corticosteroide_id").prop("disabled", true);
}

function activeDataInicioHC(){
	$("#data_inicio_hidroxicloroquina_id").prop("disabled", false);
}

function desactiveDataInicioHC(){
	$("#data_inicio_hidroxicloroquina_id").val("");
	$("#data_inicio_hidroxicloroquina_id").prop("disabled", true);
}

function dataInicioOseltamivir(){
	$("#data_inicio_oseltamivir_id").prop("disabled", false);
}

function desactiveDataInicioOseltamivir(){
	$("#data_inicio_oseltamivir_id").val("");
	$("#data_inicio_oseltamivir_id").prop("disabled", true);
}

function activeValorGlasgow(){
	if (document.getElementById("check_escala_glasgow").checked == true){
		$("#escala_glasgow_id").prop("disabled", false);
	}
	else {
		$("#escala_glasgow_id").val("");
		$("#escala_glasgow_id").prop("disabled", true);
	}
	
}

function activeBloqueadores(){
	if (document.getElementById("check_bloqueador_neuromuscular_id").checked == true){
		$("#check_midazolam").prop("disabled", false);
		$("#check_fentanil_id").prop("disabled", false);
		$("#check_propofol_id").prop("disabled", false);
		
	}
	else {
		$("#dose_midazolam_id").val("");
		$("#dose_fentanil_id").val("");
		$("#check_midazolam").prop("disabled", true);
		$("#dose_fentanil_id").prop("disabled", true);
		$("#check_midazolam").prop("checked", false);
		$("#dose_midazolam_id").prop("disabled", true);

		$("#check_fentanil_id").prop("checked", false);
		$("#check_fentanil_id").prop("disabled", true);

		$("#dose_propofol_id").val("");
		$("#dose_propofol_id").prop("disabled", true);
		$("#check_propofol_id").prop("checked", false);
		$("#check_propofol_id").prop("disabled", true);
	}

}

function activeDoseMidazolam(){
	if (document.getElementById("check_midazolam").checked == true){
		$("#dose_midazolam_id").prop("disabled", false);
	}
	else {
		$("#dose_midazolam_id").val("");
		$("#dose_midazolam_id").prop("disabled", true);
	}
}

function activeDoseFentanil(){
	if (document.getElementById("check_fentanil_id").checked == true){
		$("#dose_fentanil_id").prop("disabled", false);
	}
	else {
		$("#dose_fentanil_id").val("");
		$("#dose_fentanil_id").prop("disabled", true);
	}
}

function activeDosePropofol(){
	if (document.getElementById("check_propofol_id").checked == true){
		$("#dose_propofol_id").prop("disabled", false);
	}
	else {
		$("#dose_propofol_id").val("");
		$("#dose_propofol_id").prop("disabled", true);
	}
}

//funções para sedação continua

function activeSedacaoContinua(){
	if (document.getElementById("check_sedacao_continua_id").checked == true){
		$("#check_rocuronio_id").prop("disabled", false);
		$("#check_pancuronio_id").prop("disabled", false);
		$("#check_cisatracurio_id").prop("disabled", false);
		
	}
	else {
		$("#check_rocuronio_id").prop("disabled", true);
		$("#check_pancuronio_id").prop("disabled", true);
		$("#check_cisatracurio_id").prop("disabled", true);
		$("#check_rocuronio_id").prop("checked", false);
		$("#check_pancuronio_id").prop("checked", false);
		$("#check_cisatracurio_id").prop("checked", false);

		$("#rocuronio_dose_id").val("");
		$("#rocuronio_dose_id").prop("disabled", true);
		$("#pacuronio_dose_id").val("");
		$("#pacuronio_dose_id").prop("disabled", true);
		$("#cisatracurio_dose_id").val("");
		$("#cisatracurio_dose_id").prop("disabled", true);
	}

}

function activeDoseRocuronio(){
	if (document.getElementById("check_rocuronio_id").checked == true){
		$("#rocuronio_dose_id").prop("disabled", false);
	}
	else {
		$("#rocuronio_dose_id").val("");
		$("#rocuronio_dose_id").prop("disabled", true);
	}
}

function activeDosePacuronio(){
	if (document.getElementById("check_pancuronio_id").checked == true){
		$("#pacuronio_dose_id").prop("disabled", false);
	}
	else {
		$("#pacuronio_dose_id").val("");
		$("#pacuronio_dose_id").prop("disabled", true);
	}
}

function activeDoseCisatracurio(){
	if (document.getElementById("check_cisatracurio_id").checked == true){
		$("#cisatracurio_dose_id").prop("disabled", false);
	}
	else {
		$("#cisatracurio_dose_id").val("");
		$("#cisatracurio_dose_id").prop("disabled", true);
	}
}

function activeValorCn(){
	if (document.getElementById("check_cn_id").checked == true){
		$("#dose_cn_id").prop("disabled", false);
	}
	else {
		$("#dose_cn_id").val("");
		$("#dose_cn_id").prop("disabled", true);
	}
}

function activeValorVenturi(){
	if (document.getElementById("check_venturi_id").checked == true){
		$("#venturi_id").prop("disabled", false);
	}
	else {
		$("#venturi_id").val("");
		$("#venturi_id").prop("disabled", true);
	}
}

function activeDoseNora(){
	if (document.getElementById("check_nora_id").checked == true){
		$("#dose_nora_id").prop("disabled", false);
	}
	else {
		$("#dose_nora_id").val("");
		$("#dose_nora_id").prop("disabled", true);
	}
}

function activeDoseAdrenalina(){
	if (document.getElementById("check_adrenalina_id").checked == true){
		$("#dose_adrenalina_id").prop("disabled", false);
	}
	else {
		$("#dose_adrenalina_id").val("");
		$("#dose_adrenalina_id").prop("disabled", true);
	}
}

function activeDoseVaso(){
	if (document.getElementById("check_vasopressina_id").checked == true){
		$("#dose_vasopressina_id").prop("disabled", false);
	}
	else {
		$("#dose_vasopressina_id").val("");
		$("#dose_vasopressina_id").prop("disabled", true);
	}
}

function activeDoseDobutamina(){
	if (document.getElementById("check_dobutamina_id").checked == true){
		$("#dose_dobutamina_id").prop("disabled", false);
	}
	else {
		$("#dose_dobutamina_id").val("");
		$("#dose_dobutamina_id").prop("disabled", true);
	}
}

function activeLaudoTc(){
	if (document.getElementById("check_tc_torax_id").checked == true){
		$("#laudo_tc_torax_id").prop("disabled", false);
	}
	else {
		$("#laudo_tc_torax_id").val("");
		$("#laudo_tc_torax_id").prop("disabled", true);
	}
}

function activeLaudoRx(){
	if (document.getElementById("check_rx_torax_id").checked == true){
		$("#laudo_rx_torax_id").prop("disabled", false);
	}
	else {
		$("#laudo_rx_torax_id").val("");
		$("#laudo_rx_torax_id").prop("disabled", true);
	}
}

function activeOutroEstabelecimento(){
	if (document.getElementById("check_outros_estabelecimentos").checked == true){
		$("#outro_estabelecimento_id").prop("disabled", false);
	}
	else {
		$("#outro_estabelecimento_id").val("");
		$("#outro_estabelecimento_id").prop("disabled", true);
	}
}

//função cnes
function nomeCnes(){
	if (document.getElementById("field_cnes_id").checked == true){
		$("#nome_paciente_id").prop("disabled", true);
	}
	
}
//Fim Cnes


$(function(){

	var situacoes = [
	"AGUARDANDO CONFIRMAÇÃO DE VAGA",
	"ATUALIZADO SINAIS VITAIS",
	"NEGADO",
	"ÓBITO",
	"OUTROS",
	"PARECER MÉDICO", 
	"SEM CONDIÇÕES DE REMOÇÃO",
	"SEM VAGA",
	"SITUAÇÃO",
	"TRANSPORTE SANITÁRIO",
	];
	$("#situacao_lista_espera_id").autocomplete({
		source:situacoes
		});
});

function activeSituacao(){
	if (document.getElementById("incluir_em_lista_id").checked == true){
		$("#situacao_lista_espera_id").prop("disabled", false);

	}
	else {
		$("#situacao_lista_espera_id").val("");
		$("#situacao_lista_espera_id").prop("disabled", true);
	}
}

function desactiveSituacao(){
	$("#situacao_lista_espera_id").val("");
	$("#situacao_lista_espera_id").prop("disabled", true);
}