/**
*
* Copyright (C) 2010 Ilshad R. Khabibullin http://astoon.zwiki.org
*
* Dinamic tree and object dashboard for ice.control package.
*
**/

var LOAD_BRANCH = '@@getControlBranchTree.xml';
var TREE_CONTAINER = 'treeContainer';

var DOM_NODE = 'dom-node';
var DOM_NODE_SELF = 'dom-node-self';
var DOM_NODE_CHILDREN = 'dom-node-children';

var gBaseURL;
var gContainer;
var gTree;

// Majesty Omphalos
function TreeNode () {
    this.path = null;
    this.domNode = null;
    this.parentNode = null;
    this.childNodes = new Array();
    this.isCollapsed = true;
}

TreeNode.prototype.appendChild = function (node) {
    this.childNodes.push(node);
    var childrenDomNode = this.childrenDomNode();
    childrenDomNode.appendChild(node.domNode);
    node.parentNode = this;
}

TreeNode.prototype.load = function () {
    jQuery.ajax({type: "POST",
		 url: gBaseURL + LOAD_BRANCH,
		 dataType: "xml",
		 data: {path: this.path},
		 success: this.parse})
}

TreeNode.prototype.parse = function (xml) {
    var this_name = jQuery(

    var dom_node = this.createDiv(DOM_NODE);
    var dom_node_self = this.createDiv(DOM_NODE_SELF);
    var dom_node_children = this.createDiv(DOM_NODE_CHILDREN);

    dom_node_self.setAttribute('path', 

    dom_node.appendChild(dom_node_self);
    dom_node.appendChild(dom_node_children);

    this.domNode = dom_node;
}

TreeNode.prototype.childrenDomNode = function () {
    return this.domNode.childNodes[1];
}

TreeNode.prototype.createDiv = function (klass) {
    var node = document.createElement('div');
    node.setAttribute('class', klass);
    return node;
}

// invoked when document onload
function loadtree (root_url, base_url) {
    gBaseURL = base_url;
    gContainer = document.getElementById(TREE_CONTAINER);
    gTree = new TreeNode();
    gTree.path = root_url;
    gTree.load();
    gContainer.appendChild(gTree.domNode);
}
