//右子树少一个黑节点
var rt_iL={}
rt_iL.LLr = {
	treeName:"LLr",
	treeRoot:{
		color: "black",
		text:"G",
		leftChild:{
			color:"red",
			text:"P",
			leftChild:{
				color:"red",
				text:"U",
				leftChild:null,
				rightChild:null
			},
			rightChild:null
		},
		rightChild:{
			color:"red",
			text:"Q",
			leftChild:null,
			rightChild:null
		}
	}
};

rt_iL.LLr_result = {
	treeName:"LLr(result)",
	treeRoot:{
		color: "red",
		text:"G",
		leftChild:{
			color:"black",
			text:"P",
			leftChild:{
				color:"red",
				text:"U",
				leftChild:null,
				rightChild:null
			},
			rightChild:null
		},
		rightChild:{
			color:"black",
			text:"Q",
			leftChild:null,
			rightChild:null
		}
	}
};

rt_iL.LRr = {
	treeName:"LRr",
	treeRoot:{
		color: "black",
		text:"G",
		leftChild:{
			color:"red",
			text:"P",
			leftChild:null,
			rightChild:{
				color: "red",
				text: "U",
				leftChild: null,
				rightChild: null
			}
		},
		rightChild:{
			color:"red",
			text:"Q",
			leftChild:null,
			rightChild:null
		}
	}
};

rt_iL.LRr_result = {
	treeName:"LRr(result)",
	treeRoot:{
		color: "red",
		text:"G",
		leftChild:{
			color:"black",
			text:"P",
			leftChild:null,
			rightChild:{
				color: "red",
				text: "U",
				leftChild: null,
				rightChild: null
			}
		},
		rightChild:{
			color:"black",
			text:"Q",
			leftChild:null,
			rightChild:null
		}
	}
};

//////////////////////////////////////////////////////////

rt_iL.LLb = {
	treeName:"LLb",
	treeRoot:{
		color: "black",
		text:"G",
		leftChild:{
			color:"red",
			text:"P",
			leftChild:{
				color:"red",
				text:"U",
				leftChild:null,
				rightChild:null
			},
			rightChild:null
		},
		rightChild:{
			isNull:true,
			color:"black",
			text:"Q",
			leftChild:null,
			rightChild:null
		}
	}
};

rt_iL.LLb_result = {
	treeName:"LLb(result)",
	treeRoot:{
		color: "black",
		text:"P",
		leftChild:{
				color:"red",
				text:"U",
				leftChild:null,
				rightChild:null
			},
		rightChild:{
			color:"red",
			text:"G",
			leftChild:null,
			rightChild:{
				isNull:true,
				color:"black",
				text:"Q",
				leftChild:null,
				rightChild:null
			}
		}
	}
};

rt_iL.LRb = {
	treeName:"LRb",
	treeRoot:{
		color: "black",
		text: "G",
		leftChild:{
			color: "red",
			text:"P",
			leftChild:null,
			rightChild:{
				color: "red",
				text: "U",
				leftChild: {
					isNull:true,
					color: "black",
					text: "uL",
					leftChild: null,
					rightChild: null
				},
				rightChild: {
					isNull:true,
					color: "black",
					text: "uR",
					leftChild: null,
					rightChild: null
				}
			}
		},
		rightChild:{
			isNull:true,
			color:"black",
			text:"Q",
			leftChild:null,
			rightChild:null
		}
	}
};

rt_iL.LRb_result = {
	treeName:"LRb(result)",
	treeRoot:{
		color: "black",
		text: "U",
		leftChild:{
			color: "red",
			text:"P",
			leftChild:null,
			rightChild:{
				isNull:true,
				color: "black",
				text: "uL",
				leftChild: null,
				rightChild: null
			}
		},
		rightChild:{
			color: "red",
			text: "G",
			leftChild: {
				isNull:true,
				color: "black",
				text: "uR",
				leftChild: null,
				rightChild: null
			},
			rightChild: {
				isNull:true,
				color:"black",
				text:"Q",
				leftChild:null,
				rightChild:null
			}
		}
	}
};
