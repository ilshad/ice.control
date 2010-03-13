/**
*
* Copyright (C) 2010 Ilshad R. Khabibullin <astoon.net at gmail.com>
*
* Dynamic tree and object dashboard for ice.control package.
*
**/

var LOAD_NODE =            '@@getControlTreeNode.xml';
var LOAD_CHILDREN =        '@@getControlTreeChildren.xml';

var EXPANDED_ICON =        '++resource++mi.png';
var COLLAPSED_ICON =       '++resource++pl.png';
var SIMPLE_ICON =          '++resource++simple.png';

var TREE_CONTAINER =       'treeContainer';

var DOM_NODE =             'dom-node';
var DOM_NODE_SELF =        'dom-node-self';
var DOM_NODE_CHILDREN =    'dom-node-children';
var DOM_NODE_EXPANDER =    'dom-node-expander';
var DOM_NODE_ANCHOR =      'dom-node-anchor';
var DOM_NODE_NAME =        'dom-node-name';
var DOM_NODE_TITLE =       'dom-node-title';

var gBaseURL;
var gContainer;
var gTree;
var gNodesList;

// Majesty Omphalos
function TreeNode (path, parent) {
    this.path =         path;
    this.parentNode =   parent;
    this.domNode =      null;
    this.childNodes =   new Array();
    this.isExpanded =   true;
}

TreeNode.prototype.appendChild = function (node) {
    this.childNodes.push(node);
    var childrenDomNode = this.domNode.childNodes[1];
    childrenDomNode.appendChild(node.domNode);
    node.parentNode = this;
}

TreeNode.prototype.expand = function () {
    var exp_icon = this.createElement('img', 'src', gBaseURL + EXPANDED_ICON);
    var expander = jQuery('a.dom-node-expander', this.domNode);
    expander.empty();
    expander.append(exp_icon);
    this.isExpanded = true;
}

TreeNode.prototype.collapse = function () {
    var col_icon = this.createElement('img', 'src', gBaseURL + COLLAPSED_ICON);
    var expander = jQuery('a.dom-node-expander', this.domNode);
    expander.empty();
    expander.append(col_icon);
    this.isExpanded = false;

    node = this;
    expander.click(function () {console.log(node)})
}

TreeNode.prototype.loadNode = function (callback) {
    node = this;
    jQuery.ajax({type: "POST",
		 url: gBaseURL + LOAD_NODE,
		 dataType: "xml",
		 data: {path: this.path},
		 success: function (xml) {
		     node.parseAndBuildNode(jQuery('node', xml));
		     callback.call()
		 }})
}

TreeNode.prototype.loadChildren = function (callback) {
    node = this;
    jQuery.ajax({type: "POST",
		 url: gBaseURL + LOAD_CHILDREN,
		 dataType: "xml",
		 data: {path: this.path},
		 success: function (xml) {
		     node.parseAndBuildChildren(xml);
		     callback.call()
		 }})
}

TreeNode.prototype.parseAndBuildNode = function (xml) {
    var dom_node =           this.createElement('div', 'class', DOM_NODE);
    var dom_node_self =      this.createElement('div', 'class', DOM_NODE_SELF);
    var dom_node_children =  this.createElement('div', 'class', DOM_NODE_CHILDREN);
    var expander =           this.createElement('a', 'class', DOM_NODE_EXPANDER);
    var anchor =             this.createElement('a', 'class', DOM_NODE_ANCHOR);
    var icon =               this.createElement('img', 'src', xml.attr('icon_url'));
    var name =               this.createElement('span', 'class', DOM_NODE_NAME, xml.attr('name'));
    var title =              this.createElement('span', 'class', DOM_NODE_TITLE, xml.attr('title'));

    this.domNode = dom_node;
    dom_node_self.appendChild(expander);
    dom_node_self.appendChild(anchor);
    dom_node_self.appendChild(title);

    if (xml.attr('icon_url')) anchor.appendChild(icon);
    anchor.appendChild(name);

    dom_node.appendChild(dom_node_self);
    dom_node.appendChild(dom_node_children);

    if (parseInt(xml.attr('length')) > 0) {
	this.collapse()
    } else {
	var simple = this.createElement('img', 'src', gBaseURL + SIMPLE_ICON);
	expander.appendChild(simple);
    }

    dom_node.setAttribute('path', xml.attr('path'))
}

TreeNode.prototype.parseAndBuildChildren = function (xml, callback) {
    root = this;
    jQuery('node', xml).each(function (i) {
	var url = jQuery(this).attr('path');
	child = new TreeNode(url, root);
	child.parseAndBuildNode(jQuery(this));
	root.appendChild(child);
    })
}

TreeNode.prototype.createElement = function (type, attr_name, attr_val, inner) {
    var node = document.createElement(type);
    node.setAttribute(attr_name, attr_val);
    if (inner) jQuery(node).html(inner);
    return node;
}

// invoked when document onload
function loadtree (root_url, base_url) {
    gBaseURL = base_url;
    gContainer = document.getElementById(TREE_CONTAINER);
    gTree = new TreeNode(root_url, null);
    gTree.loadNode(function () {
	jQuery(gContainer).empty();
	gContainer.appendChild(gTree.domNode);
	gTree.expand();
	gTree.loadChildren(function () {})
    })
}
