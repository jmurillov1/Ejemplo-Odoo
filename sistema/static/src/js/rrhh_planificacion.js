
/*------------------------------
* Coloque aqui las funciones
*-------------------------------
*/
//define the odoo.define method

odoo.define('invoice.action_button', function (require) {
    "use strict";
    var core = require('web.core');
    var ListController = require('web.ListController');
    var rpc = require('web.rpc');
    var session = require('web.session');
    var _t = core._t;
    ListController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                this.$buttons.find('.my_btn_gen').click(this.proxy('action_def_generar'));
            }
        },
        action_def_generar: function () {
            var self = this
            var user = session.uid;
            self.do_action({
                name: "Generar Planificación",
                type: 'ir.actions.act_window',
                res_model: 'ges.rrhh.wizard',
                view_mode: 'form',
                view_type: 'form',
                views: [[false, 'form']],
                target: 'new',
            });
        }
    });
});

function ocultarBotones() {
    let footer_button = $('.modal-footer button');
    if (footer_button.length == 6) {
        $(footer_button.get(4)).css({ 'display': 'none' });
    } else if (footer_button.length == 3) {
        $(footer_button.get(1)).css({ 'display': 'none' });
    }
}

function validarNumCargos() {
    $('[name="numero_cargos"]').keyup(function (e) {
        let num = parseInt($('[name="numero_cargos"]').val());
        if (num < 1) {
            $('[name="numero_cargos"]').val(1);
        }
    });
}