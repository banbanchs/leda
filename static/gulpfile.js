'use strict';

var gulp = require('gulp');

var less = require('gulp-less');
var sourcemaps = require('gulp-sourcemaps');
var autoprefixer = require('gulp-autoprefixer');
var amdOptimize = require('amd-optimize');
var plumber = require('gulp-plumber');


// Less to css
gulp.task('less', function() {
  return gulp.src('./style.less')
    .pipe(sourcemaps.init())
    .pipe(plumber())
    .pipe(less())
    .pipe(autoprefixer())
    .pipe(sourcemaps.write({ sourceRoot: '/' }))
    .pipe(gulp.dest('.'));
});

gulp.task('script', function() {
  return gulp.src('./scripts/*.js')
    .pipe(amdOptimize('main', {
      paths: {
        "jquery": "//dn-staticfile.qbox.me/jquery/2.1.0/jquery.min"
      }
    }))
    .pipe(gulp.dest('dist/scripts'));
});

gulp.task('watch', function() {
  gulp.watch('./style.less', ['less']);
});

// Build
gulp.task('build', ['less']);

// Clean up
gulp.task('clean', require('del').bind(null, ['.tmp', 'dist']));

gulp.task('default', ['build', 'watch']);
