import os
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from typing import Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

SENDER = {
    "email": os.getenv('BREVO_SENDER_EMAIL', 'support@jerichohomestead.org'),
    "name": "House of Mary & Joseph"
}

# Configure Brevo API client
configuration = sib_api_v3_sdk.Configuration()
api_key = os.getenv('BREVO_API_KEY')
sender_email = os.getenv('BREVO_SENDER_EMAIL', 'support@jerichohomestead.org')

logger.info(f"Using Brevo API key: {api_key[:10]}...{api_key[-10:] if api_key else 'None'}")
logger.info(f"Full API key length: {len(api_key) if api_key else 0}")
logger.info(f"Using sender email: {sender_email}")
logger.info("Brevo API configuration initialized")

configuration.api_key['api-key'] = api_key
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

def format_currency(amount: float) -> str:
    """Format amount as currency."""
    return f"${amount:,.2f}"

def send_donation_receipt(email: str, amount: float, donation_id: int, created_at: Optional[datetime] = None) -> bool:
    """
    Send a donation receipt email using Brevo.
    
    Args:
        email: Recipient's email address
        amount: Donation amount
        donation_id: ID of the donation in database
        created_at: Timestamp of donation (optional)
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        logger.info("=== Starting donation receipt email send ===")
        logger.info(f"Recipient: {email}")
        logger.info(f"Donation ID: {donation_id}")
        logger.info(f"Amount: ${amount}")
        
        # Debug environment variables
        import os
        logger.info("=== Environment Variables ===")
        for key in ['BREVO_API_KEY', 'BREVO_SENDER_EMAIL', 'DATABASE_URL', 'STRIPE_SECRET_KEY']:
            value = os.getenv(key)
            if value:
                logger.info(f"{key} is set (length: {len(value)})")
                if key == 'BREVO_API_KEY':
                    logger.info(f"BREVO_API_KEY starts with: {value[:10]}")
            else:
                logger.error(f"{key} is NOT set")
        
        api_key = os.getenv('BREVO_API_KEY')
        if not api_key:
            logger.error("BREVO_API_KEY not found in environment variables")
            return False
        logger.info(f"Using API key (first 10 chars): {api_key[:10]}")
        subject = f"Thank You for Your Donation to House of Mary & Joseph (#{donation_id})"
        formatted_amount = format_currency(amount)
        date_str = created_at.strftime("%B %d, %Y") if created_at else datetime.now().strftime("%B %d, %Y")
        
        html_content = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <h2>Thank You for Your Generous Donation</h2>
            <p>Dear Friend,</p>
            <p>Thank you for your generous donation to the House of Mary & Joseph. Your support helps us continue our mission of helping India's homeless population.</p>
            
            <div style="background-color: #f5f5f5; padding: 20px; margin: 20px 0; border-radius: 5px;">
                <h3 style="margin-top: 0;">Donation Details:</h3>
                <p><strong>Donation ID:</strong> #{donation_id}</p>
                <p><strong>Amount:</strong> {formatted_amount}</p>
                <p><strong>Date:</strong> {date_str}</p>
            </div>
            
            <p>Your donation will help provide:</p>
            <ul>
                <li>Safe shelter for homeless individuals</li>
                <li>Nutritious meals</li>
                <li>Educational resources</li>
                <li>Healthcare assistance</li>
            </ul>
            
            <p>This email serves as your official receipt for tax purposes.</p>
            
            <p>With gratitude,<br>
            Father Diason<br>
            House of Mary & Joseph</p>
            
            <hr style="margin: 20px 0;">
            <p style="font-size: 12px; color: #666;">
                House of Mary & Joseph is a registered charitable organization.<br>
                Questions? Contact us at support@jerichohomestead.org
            </p>
        </div>
        """
        
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": email}],
            sender=SENDER,
            subject=subject,
            html_content=html_content
        )
        
        logger.info("Preparing to send email...")
        logger.info(f"Email content length: {len(html_content)} characters")
        logger.info(f"Subject: {subject}")
        
        api_instance.send_transac_email(send_smtp_email)
        logger.info(f"Donation receipt sent successfully to {email} for donation #{donation_id}")
        logger.info("=== Email send complete ===")
        return True
        
    except ApiException as e:
        logger.error(f"Error sending donation receipt to {email}: {str(e)}")
        logger.error(f"Full error response: {e.body if hasattr(e, 'body') else 'No response body'}")
        return False

def send_order_receipt(email: str, order_id: int, amount: float, product_name: str = "Product", shipping_name: Optional[str] = None,
                      shipping_address: Optional[str] = None, created_at: Optional[datetime] = None) -> bool:
    """
    Send an order receipt email using Brevo.
    
    Args:
        email: Recipient's email address
        order_id: ID of the order in database
        amount: Order amount
        shipping_name: Name for shipping (optional)
        shipping_address: Shipping address (optional)
        created_at: Timestamp of order (optional)
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        logger.info(f"Attempting to send order receipt to {email} for order #{order_id}")
        if not os.getenv('BREVO_API_KEY'):
            logger.error("BREVO_API_KEY not found in environment variables")
            return False
        subject = f"Your Order Confirmation from House of Mary & Joseph (#{order_id})"
        formatted_amount = format_currency(amount)
        date_str = created_at.strftime("%B %d, %Y") if created_at else datetime.now().strftime("%B %d, %Y")
        
        shipping_info = ""
        if shipping_name and shipping_address:
            shipping_info = f"""
            <div style="background-color: #f5f5f5; padding: 20px; margin: 20px 0; border-radius: 5px;">
                <h3 style="margin-top: 0;">Shipping Information:</h3>
                <p><strong>Name:</strong> {shipping_name}</p>
                <p><strong>Address:</strong> {shipping_address}</p>
            </div>
            """
        
        html_content = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <h2>Thank You for Your Order</h2>
            <p>Dear {shipping_name or 'Friend'},</p>
            <p>Thank you for your purchase from House of Mary & Joseph. Your support helps us continue our mission while enjoying our special collection of songs.</p>
            
            <div style="background-color: #f5f5f5; padding: 20px; margin: 20px 0; border-radius: 5px;">
                <h3 style="margin-top: 0;">Order Details:</h3>
                <p><strong>Order ID:</strong> #{order_id}</p>
                <p><strong>Amount:</strong> {formatted_amount}</p>
                <p><strong>Date:</strong> {date_str}</p>
                <p><strong>Product:</strong> {product_name}</p>
            </div>
            
            {shipping_info}
            
            <p>You will receive a separate email with your private YouTube playlist link to access your songs.</p>
            
            <p>60% of your purchase goes directly to supporting our mission of helping India's homeless population.</p>
            
            <p>With gratitude,<br>
            Father Diason<br>
            House of Mary & Joseph</p>
            
            <hr style="margin: 20px 0;">
            <p style="font-size: 12px; color: #666;">
                Questions about your order? Contact us at support@jerichohomestead.org
            </p>
        </div>
        """
        
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=[{"email": email}],
            sender=SENDER,
            subject=subject,
            html_content=html_content
        )
        
        api_instance.send_transac_email(send_smtp_email)
        logger.info(f"Order receipt sent successfully to {email} for order #{order_id}")
        return True
        
    except ApiException as e:
        logger.error(f"Error sending order receipt to {email}: {str(e)}")
        return False
