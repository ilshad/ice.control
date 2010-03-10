/**
*
* Copyright (C) 2010 Ilshad R. Khabibullin http://astoon.zwiki.org
*
* Dynamic tree and object dashboard for ice.control package.
*
**/

var LOAD_BRANCH =          '@@getControlBranchTree.xml';
var LOAD_NODE =            '@@getControlNode.xml';
var TREE_CONTAINER =       'treeContainer';

var DOM_NODE =             'dom-node';
var DOM_NODE_SELF =        'dom-node-self';
var DOM_NODE_CHILDREN =    'dom-node-children';
var DOM_NODE_EXPANDER =    'dom-node-expander';
var DOM_NODE_ANCHOR =      'dom-node-anchor';

var gBaseURL;
var gContainer;
var gTree;

// Majesty Omphalos
function TreeNode () {
    this.path =         null;
    this.domNode =      null;
    this.parentNode =   null;
    this.childNodes =   new Array();
    this.isCollapsed =  true;
}

TreeNode.prototype.appendChild = function (node) {
    this.childNodes.push(node);
    var childrenDomNode = this.childrenDomNode();
    childrenDomNode.appendChild(node.domNode);
    node.parentNode = this;
}

TreeNode.prototype.load = function (callback) {
    node = this;
    jQuery.ajax({type: "POST",
		 url: gBaseURL + LOAD_BRANCH,
		 dataType: "xml",
		 data: {path: this.path},
		 success: function (xml) {
		     node.parseAndBuild(node, xml, callback)
		 }})
}

TreeNode.prototype.parseAndBuild = function (node, xml, callback) {
    // parse context related variables from responseXML
    var this_name =          jQuery('this > name', xml).text();
    var this_url =           jQuery('this > url', xml).text();
    var this_icon_url =      jQuery('this > icon_url', xml).text();
    var this_size =          parseInt(jQuery('this > size', xml).text());
    var this_length =        parseInt(jQuery('this > length', xml).text());
    var this_is_container =  jQuery('this > size', xml).text() == 'True' ? true : false;

    // build HTML containers
    var dom_node =           this.createElement('div', DOM_NODE);
    var dom_node_self =      this.createElement('div', DOM_NODE_SELF);
    var dom_node_children =  this.createElement('div', DOM_NODE_CHILDREN);

    // build HTML details
    var expander =           this.createElement('a', DOM_NODE_EXPANDER, '&nbsp;')
    var anchor =             this.createElement('a', DOM_NODE_ANCHOR, '&nbsp;')

    dom_node_self.setAttribute('path', this_url);
    dom_node_self.appendChild(expander);
    dom_node_self.appendChild(anchor);

    dom_node.appendChild(dom_node_self);
    dom_node.appendChild(dom_node_children);

    node.domNode = dom_node;

    callback.call()

    // children nodes
    var children = jQuery('children > child', xml).each(
	function (i) {
	    //
	}
    )
}

TreeNode.prototype.childrenDomNode = function () {
    return this.domNode.childNodes[1];
}

TreeNode.prototype.createElement = function (type, klass, inner) {
    var node = document.createElement(type);
    node.setAttribute('class', klass);
    if (inner) jQuery(node).html(inner);
    return node;
}

// invoked when document onload
function loadtree (root_url, base_url) {
    gBaseURL = base_url;
    gContainer = document.getElementById(TREE_CONTAINER);
    gTree = new TreeNode();
    gTree.path = root_url;
    gTree.load(function () {
	jQuery(gContainer).empty();
	gContainer.appendChild(gTree.domNode);
    })
}
