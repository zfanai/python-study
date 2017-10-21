// Copyright 2009 FriendFeed
//
// Licensed under the Apache License, Version 2.0 (the "License"); you may
// not use this file except in compliance with the License. You may obtain
// a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations
// under the License.

$(document).ready(function() {
    if (!window.console) window.console = {};
    if (!window.console.log) window.console.log = function() {};

    // 为表单的submit时间添加函数
    $("#messageform").live("submit", function() {
        newMessage($(this));
        return false;
    });
    
    // 为表单的回车键事件添加监听函数
    // POST新消息到服务端
    $("#messageform").live("keypress", function(e) {
        if (e.keyCode == 13) {
            newMessage($(this));
            return false;
        }
    });
    
    $("#message").select();
    
    // 从服务端poll消息，服务端会保持长连接
    updater.poll();
});

function newMessage(form) {
    var message = form.formToDict();
    var disabled = form.find("input[type=submit]");
    disabled.disable();
    // POST新消息到服务端
    $.postJSON("/a/message/new", message, function(response) {
        // 服务端会返回完整的新消息
        // 在页面显示新消息
        updater.showMessage(response);
        if (message.id) {
            form.parent().remove();
        } else {
            form.find("input[type=text]").val("").select();
            disabled.enable();
        }
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

jQuery.postJSON = function(url, args, callback) {
    args._xsrf = getCookie("_xsrf");
    $.ajax({url: url, data: $.param(args), dataType: "text", type: "POST",
            success: function(response) {
        if (callback) callback(eval("(" + response + ")"));
    }, error: function(response) {
        console.log("ERROR:", response)
    }});
};

jQuery.fn.formToDict = function() {
    var fields = this.serializeArray();
    var json = {}
    for (var i = 0; i < fields.length; i++) {
        json[fields[i].name] = fields[i].value;
    }
    if (json.next) delete json.next;
    return json;
};

jQuery.fn.disable = function() {
    this.enable(false);
    return this;
};

jQuery.fn.enable = function(opt_enable) {
    if (arguments.length && !opt_enable) {
        this.attr("disabled", "disabled");
    } else {
        this.removeAttr("disabled");
    }
    return this;
};

var updater = {
    errorSleepTime: 500,
    cursor: null,

    poll: function() {
        var args = {"_xsrf": getCookie("_xsrf")};
        // 设置使用长连接从服务端poll消息时的cursor
        // 即发送新消息时，从服务端返回的message id
        if (updater.cursor) args.cursor = updater.cursor;
        // 从服务端使用长连接poll消息，并携带一个cursor
        // 返回消息则把消息显示到页面
        $.ajax({url: "/a/message/updates", type: "POST", dataType: "text",
                data: $.param(args), success: updater.onSuccess,
                error: updater.onError});
    },

    // 请求长连接ajax成功时的回调
    onSuccess: function(response) {
        try {
            updater.newMessages(eval("(" + response + ")"));
        } catch (e) {
            updater.onError();
            return;
        }
        updater.errorSleepTime = 500;
        window.setTimeout(updater.poll, 0);
    },

    onError: function(response) {
        updater.errorSleepTime *= 2;
        console.log("Poll error; sleeping for", updater.errorSleepTime, "ms");
        window.setTimeout(updater.poll, updater.errorSleepTime);
    },

    newMessages: function(response) {
        if (!response.messages) return;
        updater.cursor = response.cursor;
        var messages = response.messages;
        // cursor是最新一个消息的message id，是AJAX调用从/a/message/updates返回的
        // 设置cursor
        updater.cursor = messages[messages.length - 1].id;
        console.log(messages.length, "new messages, cursor:", updater.cursor);
        for (var i = 0; i < messages.length; i++) {
            updater.showMessage(messages[i]);
        }
    },

    showMessage: function(message) {
        // 根据message id查找重复消息
        var existing = $("#m" + message.id);
        // 如果消息已经存在则不添加
        // 这是因为在发送新消息时，服务端会把消息原封不动的返回
        // 再加上update取得的消息，就会发生消息重复
        if (existing.length > 0) return;
        var node = $(message.html);
        node.hide();
        $("#inbox").append(node);
        node.slideDown();
    }
};