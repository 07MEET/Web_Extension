"""Free price tracking using public data sources."""
import logging
import re
from typing import Optional, Dict, Any
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class PriceTracker:
    """Track product prices using free public sources."""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def get_price_history(self, product_url: str, site: str) -> Optional[Dict[str, Any]]:
        """
        Get price history for a product.
        
        Args:
            product_url: URL of the product
            site: Site name (amazon, flipkart, etc.)
            
        Returns:
            Dictionary with price history info or None
        """
        if site == "amazon":
            return self._get_amazon_price_history(product_url)
        
        return None
    
    def _get_amazon_price_history(self, product_url: str) -> Optional[Dict[str, Any]]:
        """
        Get Amazon price history using CamelCamelCamel (free HTML scraping).
        
        Note: This is best-effort. CamelCamelCamel may have anti-scraping measures.
        For production, consider using Keepa API (has free tier) or manual user input.
        """
        try:
            # Extract ASIN from Amazon URL
            asin = self._extract_asin(product_url)
            if not asin:
                logger.warning("Could not extract ASIN from URL")
                return None
            
            # Try to get data from CamelCamelCamel
            camel_url = f"https://camelcamelcamel.com/product/{asin}"
            
            try:
                response = requests.get(camel_url, headers=self.headers, timeout=10)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Try to extract price trend information
                # Note: This is fragile and depends on CamelCamelCamel's HTML structure
                price_info = {}
                
                # Look for current price
                current_price_elem = soup.find('span', {'class': 'green'})
                if current_price_elem:
                    price_info['current_price'] = current_price_elem.text.strip()
                
                # Look for lowest price
                lowest_price_elem = soup.find(text=re.compile(r'Lowest'))
                if lowest_price_elem:
                    price_info['has_history'] = True
                
                # Look for average price or price drop information
                price_drop_elem = soup.find(text=re.compile(r'drop|lower|decrease', re.I))
                if price_drop_elem:
                    price_info['trend'] = 'decreasing'
                
                if price_info:
                    return {
                        'source': 'camelcamelcamel',
                        'asin': asin,
                        'data': price_info,
                        'message': 'Limited price history available'
                    }
                
            except requests.RequestException as e:
                logger.warning(f"Could not fetch CamelCamelCamel data: {e}")
            
            # Fallback: Return generic advice
            return {
                'source': 'generic',
                'asin': asin,
                'message': 'Price history not available. Check CamelCamelCamel.com or Keepa.com manually for price trends.',
                'recommendation': 'Consider setting up price alerts or waiting for major sales events (Black Friday, Prime Day).'
            }
            
        except Exception as e:
            logger.error(f"Error getting price history: {e}")
            return None
    
    def _extract_asin(self, url: str) -> Optional[str]:
        """Extract ASIN from Amazon URL."""
        # Common Amazon URL patterns
        patterns = [
            r'/dp/([A-Z0-9]{10})',
            r'/product/([A-Z0-9]{10})',
            r'/gp/product/([A-Z0-9]{10})',
            r'\/([A-Z0-9]{10})(?:\/|\?|$)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    def get_price_recommendation(
        self,
        current_price: str,
        site: str,
        product_category: str = None
    ) -> Dict[str, Any]:
        """
        Get general price recommendation based on price and category.
        
        Args:
            current_price: Current product price
            site: E-commerce site
            product_category: Product category (electronics, furniture, etc.)
            
        Returns:
            Dictionary with price recommendations
        """
        # This provides generic advice without needing APIs
        recommendations = {
            'general_advice': '',
            'best_time_to_buy': [],
            'price_alert_suggestion': True
        }
        
        if site == "amazon":
            recommendations['general_advice'] = (
                "Amazon prices fluctuate frequently. Consider using "
                "CamelCamelCamel.com or Keepa to track price history."
            )
            recommendations['best_time_to_buy'] = [
                'Prime Day (July)',
                'Black Friday (November)',
                'Cyber Monday',
                'Prime Early Access Sale (October)'
            ]
        
        elif site == "flipkart":
            recommendations['general_advice'] = (
                "Flipkart offers competitive pricing with frequent sales. "
                "Check for bank offers, exchange discounts, and EMI options."
            )
            recommendations['best_time_to_buy'] = [
                'Big Billion Days (September/October)',
                'Republic Day Sale (January)',
                'Diwali Sale (October/November)',
                'End of Season Sales'
            ]
            recommendations['additional_tips'] = [
                'Check for SuperCoin discounts',
                'Look for exchange offers',
                'Compare with Amazon pricing',
                'Check seller ratings and reviews'
            ]
        
        # Category-specific advice
        if product_category and isinstance(product_category, str):
            if 'electronics' in product_category.lower():
                recommendations['category_advice'] = (
                    "Electronics typically drop in price before new model releases. "
                    "Check if a newer version is coming soon."
                )
            elif 'furniture' in product_category.lower():
                recommendations['category_advice'] = (
                    "Furniture prices are often negotiable, especially from "
                    "individual sellers. Check dimensions carefully."
                )
        
        return recommendations
