/**
*
* Copyright (C) 2010 Ilshad R. Khabibullin <astoon.net at gmail.com>
*
* Dynamic tree and object dashboard for ice.control package.
*
**/

var LOAD_NODE =            '@@getControlTreeNode.xml';
var LOAD_CHILDREN =        '@@getControlTreeChildren.xml';
var LOAD_MENU =            '@@getControlDetailsMenu';
var LOAD_INTROSPECTOR =    '@@getControlDetailsIntrospector';
var DETAILS_DEFAULT =      '@@getControlDetailsDefaultInfo';

var EXPANDED_ICON =        '++resource++mi.png';
var COLLAPSED_ICON =       '++resource++pl.png';
var SIMPLE_ICON =          '++resource++simple.png';

var TREE_CONTAINER =       'treeContainer';
var DETAILS_DOCK =         'treeDetailsDock';

var DOM_NODE =             'dom-node';
var DOM_NODE_SELF =        'dom-node-self';
var DOM_NODE_CHILDREN =    'dom-node-children';
var DOM_NODE_EXPANDER =    'dom-node-expander';
var DOM_NODE_ANCHOR =      'dom-node-anchor';
var DOM_NODE_NAME =        'dom-node-name';
var DOM_NODE_TITLE =       'dom-node-title';
var WITHOUT_ICON =         'anchor-without-icon';
var DETAILS =              'details';
var DETAILS_WRAP =         'details-wrap';
var DETAILS_HEAD =         'details-head';
var DETAILS_CLOSE =        'details-close';
var DETAILS_MINIMIZE =     'details-minimize';
var DETAILS_MENU =         'details-menu';
var DOCK =                 'dock';
var URL =                  'url';

var gBaseURL;
var gContainer;
var gTree;
var gNodesList;

// Majesty Omphalos
function TreeNode (path, parent) {
    this.path =         path;
    this.parentNode =   parent;
    this.childNodes =   new Array();
    this.name =         null;
    this.title =        null;
    this.domNode =      null;
    this.isExpanded =   null;
    this.dock =         null;
}

TreeNode.prototype.appendChild = function (dom, node) {
    this.childNodes.push(node);
    dom.appendChild(node.domNode);
    node.parentNode = this;
}

TreeNode.prototype.nodeLookUp = function () {
    var ext_nodes = [this.domNode];
    var ex_height = [$(this.domNode).height()];
    $(this.domNode).parents('div.dom-node').each(function (i) {
	ext_nodes.push(this);
	ex_height.push($(this).height());
    });
    return {ext_nodes: ext_nodes,
	    ex_height: ex_height}
}

TreeNode.prototype.expand = function () {
    var dom_children = this.createElement('div', 'class', DOM_NODE_CHILDREN);
    $(this.domNode.childNodes[0]).after(dom_children);
    
    var ex = this.nodeLookUp();

    var node = this;
    this.loadChildren(dom_children, function () {
	var h = $(dom_children).height();
	$(ex.ext_nodes).each(function (i) {
	    $(this).height(ex.ex_height[i] + h);
	});
    });

    var exp_icon = this.createElement('img', 'src', gBaseURL + EXPANDED_ICON);
    var expander = $('a.dom-node-expander', this.domNode);
    expander.empty();
    expander.append(exp_icon);
    this.isExpanded = true;
}

TreeNode.prototype.collapse = function () {
    var dom_children = this.domNode.childNodes[1];
    var h = $(dom_children).height();
    var ex = this.nodeLookUp();
    
    $(dom_children).remove();

    $(ex.ext_nodes).each(function (i) {
	$(this).height(ex.ex_height[i] - h);
    });

    var col_icon = this.createElement('img', 'src', gBaseURL + COLLAPSED_ICON);
    var expander = $('a.dom-node-expander', this.domNode);
    expander.empty();
    expander.append(col_icon);
    this.isExpanded = false;
}

TreeNode.prototype.loadNode = function (callback) {
    var node = this;
    $.ajax({type: "POST",
	    url: node.path + LOAD_NODE,
	    dataType: "xml",
	    data: {},
	    success: function (xml) {
		node.parseAndBuildNode($('node', xml));
		callback.call()
	    }})
}

TreeNode.prototype.loadChildren = function (dom, callback) {
    var node = this;
    $.ajax({type: "POST",
	    url: node.path + LOAD_CHILDREN,
	    dataType: "xml",
	    data: {},
	    success: function (xml) {
		node.parseAndBuildChildren(dom, xml);
		callback.call()
	    }})
}

TreeNode.prototype.parseAndBuildNode = function (xml) {
    this.name = xml.attr('name') || 'root';
    this.title = xml.attr('title');

    var dom_node = this.createElement('div', 'class', DOM_NODE);
    var dom_node_self = this.createElement('div', 'class', DOM_NODE_SELF);
    var expander = this.createElement('a', 'class', DOM_NODE_EXPANDER);
    var anchor = this.createElement('a', 'class', DOM_NODE_ANCHOR);
    var icon = this.createElement('img', 'src', xml.attr('icon_url'));
    var name = this.createElement('span', 'class', DOM_NODE_NAME, this.name);
    var title = this.createElement('span', 'class', DOM_NODE_TITLE, this.title);

    this.domNode = dom_node;

    dom_node_self.appendChild(expander);
    dom_node_self.appendChild(anchor);
    dom_node_self.appendChild(title);

    if (xml.attr('icon_url')) { anchor.appendChild(icon) }
    else { $(anchor).addClass(WITHOUT_ICON) }

    anchor.appendChild(name);

    dom_node.appendChild(dom_node_self);
    dom_node.setAttribute('style', 'display: block');

    if (parseInt(xml.attr('length')) > 0) {
	expander.appendChild(
	    this.createElement('img', 'src', gBaseURL + COLLAPSED_ICON));
	this.isExpanded = false;
    } else {
	expander.appendChild(
	    this.createElement('img', 'src', gBaseURL + SIMPLE_ICON));
    }
    
    // Click it
    var node = this;
    expander.onclick = function () {
	if (node.isExpanded == null) {return false}
	if (node.isExpanded == true) {node.collapse(); return false}
	if (node.isExpanded == false) {node.expand(); return false}
    }
    anchor.onclick = function () {
	if (node.dock != null) {
	    $(node.dock).click();
	} else {
	    node.openDetails();
	}
    }

    // Identify me explicity
    dom_node.setAttribute('path', xml.attr('path'));
}

TreeNode.prototype.parseAndBuildChildren = function (dom, xml) {
    var root = this;
    $('node', xml).each(function (i) {
	var url = $(this).attr('path');
	child = new TreeNode(url, root);
	child.parseAndBuildNode($(this));
	root.appendChild(dom, child);
    })
}

// click on Details Menu
function loadControlDetails (url, data, node, callback) {
    var detailsWrap = node.parentNode.parentNode.childNodes[1];
    $(detailsWrap).load(url, {}, function () {
	// submit Form
	$('input:submit', detailsWrap).click(function () {
	    var form = $(this).parents('form')[0];
	    var params = $(form).serialize();
	    params = params.concat('&' + this.name + '=' + this.value)
	    loadControlDetails(form.action, params, node);
	    return false;
	});

	// click link
	$('a', detailsWrap).click(function () {
	    var href = $(this).attr('href'); // original, not generated by browser

	    // introspector
	    if ($(this).parents('#introspector').length > 0) {

		// open ++apidoc++ links in new window
		if (href.indexOf("++apidoc++") >= 0) {
		    window.open(href, "", "scrollbars");
		    return false;
		}

		// replace @@introspector.html -> @@getControlDetailsIntrospector
		var ispct = href.indexOf("@@introspector.html");
		if (ispct > 0) {
		    href = href.slice(0, ispct) + LOAD_INTROSPECTOR;
		}
	    }

	    // add context path when relative url
	    if (href.indexOf("http") != 0) {
		var context_url = $('span.url',
				    $(this)
				    .parents("div." + DETAILS)
				    .children("div." + DETAILS_HEAD)).text();
		href = context_url.concat(href);
	    }
	    loadControlDetails(href.split("?")[0], href.split("?")[1], node);
	    return false;
	});

	if (callback) callback.call();
    });
}

TreeNode.prototype.openDetails = function () {
    var details = this.createElement('div', 'class', DETAILS);
    var detailsWrap = this.createElement('div', 'class', DETAILS_WRAP, '&nbsp');
    var detailsHead = this.createElement('div', 'class', DETAILS_HEAD, '&nbsp');
    var detailsClose = this.createElement('a', 'class', DETAILS_CLOSE, 'X');
    var detailsMinimize = this.createElement('a', 'class', DETAILS_MINIMIZE, '_');
    var detailsMenu = this.createElement('div', 'class', DETAILS_MENU, '&nbsp;');
    var url = this.createElement('span', 'class', URL, this.path);

    var node = this;

    detailsClose.onclick = function () {
	$(details).fadeOut("normal", function() {
	    $(details).remove();
	    if (node.dock != null) {
		$(node.dock).remove()
		node.dock = null;
	    }
	    node.refresh();
	});
    }

    detailsMinimize.onclick = function () {
	node.minimizeDetails(details);
	node.refresh();
    }
    
    var path = this.path;
    $(details)
	.prependTo($('#' + TREE_CONTAINER))
	.append($(detailsWrap))
	.append($(detailsMenu))
	.fadeIn("normal", function () {
	    $(detailsWrap).load(path + DETAILS_DEFAULT, {}, function () {
		// behavior on default view
	    });

	    $(detailsMenu).load(path + LOAD_MENU);
	});

    $(detailsHead)
	.prependTo($(details))
	.append($(detailsClose))
	.append($(detailsMinimize))
	.append($(url));
}

TreeNode.prototype.minimizeDetails = function (details) {
    $(details).slideUp();

    if (this.dock == null) {
	var dock = this.createElement('div', 'class', DOCK, this.name);
	var dock_box = document.getElementById(DETAILS_DOCK);
	$(dock).appendTo($(dock_box));
	dock.onclick = function () { $(details).slideDown() }
	this.dock = dock;
    }
}

TreeNode.prototype.refresh = function () {
    var node = this;
    $.ajax({type: "POST",
	    url: node.path + LOAD_NODE,
	    dataType: "xml",
	    data: {},
	    success: function (xml) {
		description = $('node', xml);
		var title = description.attr('title');
		if (title != node.title) {
		    node.title = title;
		    $('span.' + DOM_NODE_TITLE,
		      node.domNode.childNodes[0]).text(title);
		}
	    }})
}

TreeNode.prototype.createElement = function (type, attr_name, attr_val, inner) {
    var node = document.createElement(type);
    node.setAttribute(attr_name, attr_val);
    if (inner)
	$(node).html(inner);
    return node;
}

// onload document
function loadtree (root_url, base_url) {
    gBaseURL = base_url;
    gContainer = document.getElementById(TREE_CONTAINER);
    gTree = new TreeNode(root_url, null);
    gTree.loadNode(function () {
	$(gContainer).empty();
	gContainer.appendChild(gTree.domNode);
	gTree.expand();
    })
}

// Loading...
$(function () {
    $("#spinner").ajaxStart(
	function () {$(this).show()}
    ).ajaxStop(
	function () {$(this).hide()});
});
