//右子树少一个黑节点
var rt_iR={}
rt_iR.RRr = {
	treeName:"RRr",
	treeRoot:{
		color: "black",
		text:"G",
		leftChild:{
			color:"red",
			text:"Q",
			leftChild:null,
			rightChild:null
		},
		rightChild:{
			color:"red",
			text:"P",
			leftChild:null,
			rightChild:{
				color:"red",
				text:"U",
				leftChild:null,
				rightChild:null
			}
		}
	}
};

rt_iR.RRr_result = {
	treeName:"RRr(result)",
	treeRoot:{
		color: "red",
		text:"G",
		leftChild:{
			color:"black",
			text:"Q",
			leftChild:null,
			rightChild:null
		},
		rightChild:{
			color:"black",
			text:"P",
			leftChild:null,
			rightChild:{
				color:"red",
				text:"U",
				leftChild:null,
				rightChild:null
			}
		}
	}
};

rt_iR.RLr = {
	treeName:"RLr",
	treeRoot:{
		color: "black",
		text:"G",
		leftChild:{
			color:"red",
			text:"Q",
			leftChild:null,
			rightChild:null
		},
		rightChild:{
			color:"red",
			text:"P",
			leftChild:{
				color: "red",
				text: "U",
				leftChild: null,
				rightChild: null
			},
			rightChild:null
		}
	}
};

rt_iR.RLr_result = {
	treeName:"RLr(result)",
	treeRoot:{
		color: "red",
		text:"G",
		leftChild:{
			color:"black",
			text:"Q",
			leftChild:null,
			rightChild:null
		},
		rightChild:{
			color:"black",
			text:"P",
			leftChild:{
				color: "red",
				text: "U",
				leftChild: null,
				rightChild: null
			},
			rightChild:null
		}
	}
};

//////////////////////////////////////////////////////////

rt_iR.RRb = {
	treeName:"RRb",
	treeRoot:{
		color: "black",
		text:"G",
		leftChild:{
			isNull:true,
			color:"black",
			text:"Q",
			leftChild:null,
			rightChild:null
		},
		rightChild:{
			color:"red",
			text:"P",
			leftChild:null,
			rightChild:{
				color:"red",
				text:"U",
				leftChild:null,
				rightChild:null
			}
		}
	}
};

rt_iR.RRb_result = {
	treeName:"RRb_result",
	treeRoot:{
		color: "black",
		text:"P",
		leftChild:{
			color:"red",
			text:"G",
			leftChild:{
				isNull:true,
				color:"black",
				text:"Q",
				leftChild:null,
				rightChild:null
			},
			rightChild:null
		},
		rightChild:{
			color:"red",
			text:"U",
			leftChild:null,
			rightChild:null
		}
	}
};

rt_iR.RLb = {
	treeName:"RLb",
	treeRoot:{
		color: "black",
		text: "G",
		leftChild:{
			isNull:true,
			color:"black",
			text:"Q",
			leftChild:null,
			rightChild:null
		},
		rightChild:{
			color: "red",
			text:"P",
			leftChild:{
				color: "red",
				text: "U",
				leftChild:{
					isNull:true,
					color: "black",
					text: "uR",
					leftChild: null,
					rightChild: null
				},
				rightChild:{
					isNull:true,
					color: "black",
					text: "uL",
					leftChild: null,
					rightChild: null
				}
			},
			rightChild:null
		}
	}
};

rt_iR.RLb_result = {
	treeName:"LRb(result)",
	treeRoot:{
		color: "black",
		text: "U",
		leftChild:{
			color: "red",
			text: "G",
			leftChild: {
				isNull:true,
				color:"black",
				text:"Q",
				leftChild:null,
				rightChild:null
			},
			rightChild: {
				isNull:true,
				color: "black",
				text: "uR",
				leftChild: null,
				rightChild: null
			}
		},
		rightChild:{
			color: "red",
			text:"P",
			leftChild:{
				isNull:true,
				color: "black",
				text: "uL",
				leftChild: null,
				rightChild: null
			},
			rightChild:null
		}
	}
};

