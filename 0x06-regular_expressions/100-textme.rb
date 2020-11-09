#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:|to:|flags:)(\w+|\+?\d+|-?\d:-?\d:-?\d:-?\d:-?\d)/).join(',')
