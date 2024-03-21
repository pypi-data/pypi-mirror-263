# get a bunch of entry caption files based on entries in a mediaspace channel playlists

require 'kaltura'
require 'nokogiri'
require 'open-uri'
require 'pry'

include Kaltura

# function to start Kaltura session
def get_kaltura_session(partnerID, adminkey, client)
  secret = adminkey
  user_id = nil
  type = KalturaSessionType::ADMIN
  expiry = 1800  #3 hours
  privileges = 'disableentitlement'

  ks = client.session_service.start(secret, user_id, type, partnerID, expiry, privileges)
  ks
end

partnerID = 'your_partner_id_goes_here'
adminkey = 'your_admin_key_goes_here'

config = KalturaConfiguration.new
config.service_url = 'https://www.kaltura.com'
client = KalturaClient.new(config)
# client.ks = get_kaltura_session(partnerID, adminkey, client)
client.ks = 'MTBlNjgzZDk3YjVmYzZlZmQ3NmQ4NWY2MWYwZjUxN2M1N2FhMjJhN3wxMDM4NDcyOzEwMzg0NzI7MjgyODAwMzkzMzsyOzE0MDc5NTM5ODkuMjU1OztkaXNhYmxlZW50aXRsZW1lbnQ7Ow=='


filter = KalturaMetadataFilter.new
filter.metadata_object_type_equal = KalturaMetadataObjectType::CATEGORY
filter.object_id_equal = '333421872'
# 2023-2024 category IDs 304973402, 309256382, 316800112, 322521492, 333421872
filter.metadata_profile_id_equal = 1407602
pager = KalturaFilterPager.new

#get the playlist IDs from the category metadata
results = client.metadata_service.list(filter, pager)

if results.objects.respond_to?('first')
  metadata_doc = Nokogiri::XML(results.objects.first.xml)
  playlist_ids = metadata_doc.xpath("//metadata/Detail/Key[text()='channelPlaylistsIds']/following-sibling::*[1]").text
  playlist_ids = playlist_ids.split(',')
end

#iterate over each playlist in the channel
playlist_ids.each do |p|

  version = -1

  pl_results = client.playlist_service.get(p, version)
  pl_name = pl_results.name
  pl_entries = pl_results.playlist_content.split(',')

  #iterate over each entry in the playlist
  pl_entries.each do |e|
    entry_results = client.base_entry_service.get(e, version)
    entry_name = entry_results.name

    puts e
    puts entry_name

    aalist_filter = KalturaAttachmentAssetFilter.new
    aalist_filter.format_equal = KalturaAttachmentType::TEXT
    aalist_filter.entry_id_equal = e
    aalist_pager = KalturaFilterPager.new

    #check for a plaintext caption file attachement
    aalist_results = client.attachment_asset_service.list(aalist_filter, aalist_pager)

    storage_id = nil

    if aalist_results.total_count != 0
      puts 'getting caption text file'
      aaget_results = client.attachment_asset_service.get_url(aalist_results.objects[0].id, storage_id)
      puts aaget_results

      filename = pl_name.gsub(' ', '_') + '_' + entry_name.gsub(' ', '_').gsub('/', '_')

      puts filename

      download = URI.open(aaget_results)
      IO.copy_stream(download, "/Users/rjmcinty/omse/#{filename}.txt")
    else
      puts 'no captions plaintext file, getting regular captions'
      #get the caption file and parse it

      filter = KalturaAssetFilter.new
      filter.entry_id_equal = e
      pager = KalturaFilterPager.new

      caption_results = client.caption_asset_service.list(filter, pager)
      puts caption_results.inspect
      if caption_results.total_count == 0
        puts 'no caption files available'
      else
        caption_results.objects.each do |c|
          if c.file_ext == 'dfxp'
            captions = client.caption_asset_service.serve(c.id)
            caption_file_doc = Nokogiri::XML(URI.open(captions))

            filename = pl_name.gsub(' ', '_') + '_' + entry_name.gsub(' ', '_').gsub('/', '_')

            puts filename

            #gather just the <p> nodes for the actual captions and write out to file
            IO.write("/Users/rjmcinty/omse/#{filename}.txt", caption_file_doc.css('p').map(&:text).join(' ').gsub(/\n/, ''))
          elsif c.file_ext == 'srt'
            captions = client.caption_asset_service.serve(c.id)
            caption_file_doc = URI.open(captions).read

            caption_file_doc = caption_file_doc.gsub(/((.*(\n|\r|\r\n)){2}).*-->.*/, '').lines[2..-1].join.gsub(/\R+/, ' ')

            #remove all the SRT timings and other gunk
            filename = pl_name.gsub(' ', '_') + '_' + entry_name + '_srt'.gsub(' ', '_').gsub('/', '_')

            puts filename

            IO.write("/Users/rjmcinty/omse/#{filename}.txt", caption_file_doc)
          else
            puts 'no caption files available'
          end
        end
      end

    end
    puts ''
  end
end
