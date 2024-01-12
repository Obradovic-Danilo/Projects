# Task guide
> This is a guide which describes how to initialize, configure and start boilerplate code that you will use in order to complete the task that is given to you.

> Codebase is set up and managed using [Webpack4](https://webpack.js.org/)

When it comes to app functionalities, you have to enable a feature where when you click on the menu icon, __sidebar should appear aside__.

In order to see how the result of the task should look like, visit these two links:

https://youtu.be/tGN1Vh49iU0 (Desktop version)

https://youtu.be/nYHa31hRkhg (Mobile version)

Required design for website is located in a __design_prototype__ folder where desktop and mobile version are provided along with style guide (font sizes and color palette).

All other requirements and information for the task are provided to you via email.

**The code structure is already set up with appropriate assets**

**index.html* is located in a *dist* folder where it's content should be added.**

Javascript code has to be written in an **src/js/scripts.js** file.

All your styles have to be written in an **src/css/style.scss** file and __writing them as SASS code will be considered as a plus__.

After you complete the task, you have to pack whole folder __EXCLUDING the node_modules FOLDER__ using ZIP or TAR.GZ and send it to us via following URL https://dcdrive.digitalcube.rs/ 

The requested CODE is case sensitive code which can be found in the initial email.

## Setup

### Requirements

Node `">=5.0.0"` you can install it from [here](http://nodejs.org/)


### Clone the repository

```bash
git clone https://github.com/digital-cube/html-test.git
cd html-test
```

### Dependencies

To get a project working, you have to install all it's dependencies with the following command:

```bash
npm install
```

## Configuration

### Adding third party libraries (optional)


__Note that jQuery is already included in this boilerplate code by default, but you can append additional libraries if necessary.__


If you want to use third party libraries, you should first install them via **npm install library_name --save**

You can provide them as plugins by registering them in __webpack.dev.config.js__ file.

In this example jQuery and momentjs are appended in a PLUGINS array where you define it's alias names that will be used in your code.


```
const PLUGINS = [
    new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery',
        moment: 'moment',
    })
];
```


Since you have registered third party libraries in this configuration file, you can use them straightforward **without having to import them explicitly** in a __js/scripts.js__ file.



## Running

Following command starts a project on the given port, recompiles it on detected changes in the code and reloads browser

```bash
npm run start
```

