goog.provide('vk2.utils');

goog.require('goog.dom');
goog.require('goog.dom.classes');

/**
 * This function checks if cookies are enabled
 * @static
 */
vk2.utils.checkIfCookiesAreEnabble = function(){
	if (!navigator.cookieEnabled){
		alert('This page needs cookies for correct behavior. So please activate them in your browser.');
	} else if (goog.DEBUG) {
		console.log('Cookies are enabled');		
	}
};

/**
 * @param {Element} element
 * @param {string} className
 */
vk2.utils.getClosestParentElementForClass = function(element, className){
	var element = goog.dom.classes.has(element, className) ? element : 
		this.getClosestParentElementForClass(goog.dom.getParentElement(element), className);
	return element;
};

/**
 * 
 * This function encapsulate the json lang_dictionary from the locale javascript folder.
 * @static
 * @param key - {String}
 * @return {String}
 */
vk2.utils.getMsg = function(key){
	try{
		if (goog.isDef(window['lang_dictionary'])) return window['lang_dictionary'][key];
	} catch (ReferenceError){
		console.log('Could not found dictionary.');
		return '';
	}
};

/**
 * @param {Array.<number>} extent
 * @return {Array.<Array.<number>>}
 */
vk2.utils.getPolygonFromExtent = function(extent){
	return [[extent[0],extent[1]], [extent[0],extent[3]], [extent[2],extent[3]], [extent[2],extent[1]]];
};

/**
 * @param {string} dateiname
 * @return {string}
 */
vk2.utils.generateMesstischblattThumbnailLink = function(dateiname){
	return vk2.settings.THUMBNAIL_URL+dateiname+'.jpg';
};
