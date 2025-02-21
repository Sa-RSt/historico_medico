$(function() {

    refreshMedicos();

});

function refreshMedicos() {
    fetch('/api/medicos')
        .then(resp => resp.json())
        .then(data => {
            if (data.erro === null) {
                let profs = data.resultado;
                
                $('#o_tbody').empty();
                
                for (let prof of profs) {
                    let lg = $('<tr class="table-primary"></tr>');
                    for (let attr of [prof.id, prof.crm, prof.nome_social, prof.nome_civil, prof.profissao]) {
                        let li = $('<td></td>');
                        if (attr === null) {
                            li.text('N/A');
                            li.addClass('text-muted');
                        } else {
                            li.text(attr);
                        }
                        lg.append(li);
                    }
                    $('#o_tbody').append(lg);
                }
            } else {
                const msg = $('<h3></h3>');
                msg.text('Erro: ' + data.erro);
                msg.addClass('text-danger');
                $('#o_tbody').empty();
                $('#o_tbody').append(msg);
            }
        });
}
