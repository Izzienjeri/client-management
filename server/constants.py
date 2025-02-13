class LeadStatus:
    NEW_LEAD = "New Lead"
    CONTACTED = "Contacted"
    QUALIFIED = "Qualified"
    NOT_QUALIFIED = "Not Qualified"
    DISCOVERY_PHASE = "Discovery Phase"
    PROPOSAL_SENT = "Proposal Sent"
    NEGOTIATION = "Negotiation"
    CONTRACT_SIGNED = "Contract Signed"
    PROJECT_STARTED = "Project Started"
    IN_PROGRESS = "In Progress"
    UNDER_REVIEW = "Under Review"
    COMPLETED = "Completed"
    LAUNCHED = "Launched"

    CHOICES = [
        NEW_LEAD, CONTACTED, QUALIFIED, NOT_QUALIFIED, DISCOVERY_PHASE, PROPOSAL_SENT,
        NEGOTIATION, CONTRACT_SIGNED, PROJECT_STARTED, IN_PROGRESS, UNDER_REVIEW, COMPLETED, LAUNCHED
    ]
