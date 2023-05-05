#!/usr/bin/env ruby

puts ARGV[0].scan(/from:[^\]]+/)[0].split(':')[1] + "," + \
	 ARGV[0].scan(/to:[^\]]+/)[0].split(':')[1] + ","  + \
	 ARGV[0].scan(/flags:[^\]]+/)[0][6..]
