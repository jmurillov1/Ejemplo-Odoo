/*------------------------------
 * Coloque aqui las funciones
 *-------------------------------
 */
//define the odoo.define method

odoo.define('invoice.action_button', function(require) {
    "use strict";
    var core = require('web.core');
    var ListController = require('web.ListController');
    var rpc = require('web.rpc');
    var session = require('web.session');
    var _t = core._t;
    ListController.include({
        renderButtons: function($node) {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                this.$buttons.find('.my_btn_cre').click(this.proxy('action_def_crear'));
            }
        },
        action_def_crear: function() {
            var self = this;
            var user = session.uid;
            rpc.query({
                model: 'ges.rrhh.partida',
                method: 'crear_partidas',
                args: [
                    [user], { 'id': user }
                ],
            }).then(function(res) {
                if (res == false) {
                    self.do_notify("Advertencia", "Ya hay creadas partidas, si quiere actualizar haga click en Actualizar Partidas", true);
                } else {
                    self.trigger_up('reload');
                }
            }).catch(e => {
                console.log(e);
            });
        }
    });
});

odoo.define('invoice.action_button', function(require) {
    "use strict";
    var core = require('web.core');
    var ListController = require('web.ListController');
    var rpc = require('web.rpc');
    var session = require('web.session');
    var _t = core._t;
    ListController.include({
        renderButtons: function($node) {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                this.$buttons.find('.my_btn_act').click(this.proxy('action_def_actualizar'));
            }
        },
        action_def_actualizar: function() {
            var self = this
            var user = session.uid;
            rpc.query({
                model: 'ges.rrhh.partida',
                method: 'actualizar_partidas',
                args: [
                    [user], { 'id': user }
                ],
            }).then(function(res) {
                self.trigger_up('reload');
            }).catch(e => {
                console.log(e);
            });
        }
    });
});