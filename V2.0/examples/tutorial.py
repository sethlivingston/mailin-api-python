from mailin import Mailin

m = Mailin("https://api.sendinblue.com/v2.0","access key")
campaigns = m.get_campaigns_v2('classic') # to retrieve all campaigns of type 'classic'
campaigns = m.get_campaigns_v2('') # to retrieve all campaigns
