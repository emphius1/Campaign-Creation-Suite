```javascript
document.getElementById('campaign_orchestrator').addEventListener('click', function() {
    // Import necessary dependencies
    const campaignSettings = require('../shared_dependencies/exported_variables').campaign_settings;
    const createCampaign = require('../shared_dependencies/function_names').createCampaign;
    const CampaignCreated = require('../shared_dependencies/message_names').CampaignCreated;

    // Create a new campaign
    let newCampaign = createCampaign(campaignSettings);

    // Dispatch a message to notify that a new campaign has been created
    let event = new CustomEvent(CampaignCreated, { detail: newCampaign });
    document.dispatchEvent(event);
});
```