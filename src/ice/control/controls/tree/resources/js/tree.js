/**
*
* Copyright (C) 2010 Ilshad R. Khabibullin http://astoon.zwiki.org
*
* Dinamic tree and object dashboard for ice.control package.
*
**/

var LOAD_BRANCH = '@@loadBranch.xml';
var TREE_CONTAINER = 'treeContainer';

var gBaseURL;
var gContainer;
var gTree;

// This XML grammar defines contents tree
var contentsTreeXMLGrammar = {
    
}

// Tokenizer / lexical analyser generator
function Lexer (grammar) {
}

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
    this.domNode.appendChild(node.domNode);
    node.parentNode = this;
}

TreeNode.prototype.load = function () {
    jQuery.ajax({type: "POST",
		 url: gBaseURL + LOAD_BRANCH,
		 dataType: "xml",
		 data: {path: this.path},
		 success: this.parseAndCompile})
}

// XML --> HTML
TreeNode.prototype.parseAndCompile = function (xml) {
    // parse
    lexer = new Lexer(contentsTreeXMLGrammar);
    var tokens = jQuery.map(
	jQuery("document", xml).children(),
	lexer.tokenize);
    // compile
    for (var item in tokens) {
	if (item.
}

// invoked when document onload
function loadtree (root_url, base_url) {
    gBaseURL = base_url;
    gContainer = document.getElementById(TREE_WRAPPER);
    gTree = new TreeNode();
    gTree.path = root_url;
    gTree.load();
    gContainer.appendChild(gTree.domNode);
}
