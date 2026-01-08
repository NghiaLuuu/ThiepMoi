from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math

def create_gradient_background(width, height):
    """Create an elegant gradient background"""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    # Create a sophisticated vertical gradient (deep navy to teal)
    for y in range(height):
        # Smooth gradient from deep blue to teal
        ratio = y / height
        r = int(15 + (32 - 15) * ratio)
        g = int(32 + (178 - 32) * ratio)
        b = int(89 + (170 - 89) * ratio)
        draw.rectangle([0, y, width, y+1], fill=(r, g, b))
    
    return image

def draw_elegant_decoration(draw, width, height):
    """Draw elegant geometric decorations"""
    # Draw subtle corner decorations
    accent_color = (255, 215, 0, 100)  # Gold with transparency
    
    # Top left corner arc
    for i in range(3):
        offset = i * 15
        draw.arc([50 + offset, 50 + offset, 250 - offset, 250 - offset], 
                 start=180, end=270, fill=(255, 215, 0), width=2)
    
    # Top right corner arc
    for i in range(3):
        offset = i * 15
        draw.arc([width - 250 + offset, 50 + offset, width - 50 - offset, 250 - offset], 
                 start=270, end=360, fill=(255, 215, 0), width=2)
    
    # Bottom left corner arc
    for i in range(3):
        offset = i * 15
        draw.arc([50 + offset, height - 250 + offset, 250 - offset, height - 50 - offset], 
                 start=90, end=180, fill=(255, 215, 0), width=2)
    
    # Bottom right corner arc
    for i in range(3):
        offset = i * 15
        draw.arc([width - 250 + offset, height - 250 + offset, width - 50 - offset, height - 50 - offset], 
                 start=0, end=90, fill=(255, 215, 0), width=2)
    
    # Add subtle sparkle points
    sparkle_points = [
        (width // 2, 120),
        (200, 400),
        (width - 200, 400),
        (width // 2, height - 150),
        (250, height // 2),
        (width - 250, height // 2)
    ]
    
    for x, y in sparkle_points:
        # Draw small diamond shape
        size = 8
        points = [(x, y - size), (x + size, y), (x, y + size), (x - size, y)]
        draw.polygon(points, fill=(255, 215, 0))

def draw_text_with_shadow(draw, position, text, font, text_color, shadow_color, shadow_offset=(2, 2)):
    """Draw text with a subtle shadow effect"""
    x, y = position
    # Draw shadow
    draw.text((x + shadow_offset[0], y + shadow_offset[1]), text, font=font, fill=shadow_color)
    # Draw main text
    draw.text((x, y), text, font=font, fill=text_color)


def create_birthday_invitation():
    """Create an elegant birthday invitation card"""
    # Card dimensions
    width, height = 1200, 1600
    
    # Create gradient background
    image = create_gradient_background(width, height)
    draw = ImageDraw.Draw(image)
    
    # Add elegant decorations
    draw_elegant_decoration(draw, width, height)
    
    # Add elegant border frame
    border_margin = 40
    draw.rectangle([border_margin, border_margin, width - border_margin, height - border_margin], 
                   outline=(255, 215, 0), width=3)
    
    # Inner frame
    inner_margin = 55
    draw.rectangle([inner_margin, inner_margin, width - inner_margin, height - inner_margin], 
                   outline=(255, 215, 0, 150), width=1)
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 75)
        name_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 85)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 42)
        detail_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 38)
    except:
        title_font = ImageFont.load_default()
        name_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        detail_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    
    center_x = width // 2
    
    # Top decorative line
    line_width = 400
    draw.line([center_x - line_width//2, 180, center_x + line_width//2, 180], 
              fill=(255, 215, 0), width=2)
    
    # Title: "BIRTHDAY CELEBRATION"
    title_text = "BIRTHDAY CELEBRATION"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw_text_with_shadow(draw, (center_x - title_width//2, 210), title_text, 
                         title_font, (255, 255, 255), (0, 0, 0, 100), shadow_offset=(2, 2))
    
    # Decorative separator
    y_pos = 320
    separator_width = 300
    draw.line([center_x - separator_width//2, y_pos, center_x + separator_width//2, y_pos], 
              fill=(255, 215, 0), width=2)
    
    # Name (prominent)
    name_text = "LƯU TRUNG NGHĨA"
    name_bbox = draw.textbbox((0, 0), name_text, font=name_font)
    name_width = name_bbox[2] - name_bbox[0]
    draw_text_with_shadow(draw, (center_x - name_width//2, 370), name_text, 
                         name_font, (255, 215, 0), (0, 0, 0, 120), shadow_offset=(3, 3))
    
    # Subtitle
    subtitle_text = "kính mời quý khách đến dự"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text((center_x - subtitle_width//2, 490), subtitle_text, 
              font=subtitle_font, fill=(220, 220, 220))
    
    # Main invitation box
    box_top = 600
    box_height = 480
    box_margin = 100
    
    # Create elegant box with border
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    # Draw box background with slight transparency
    overlay_draw.rounded_rectangle(
        [box_margin, box_top, width - box_margin, box_top + box_height],
        radius=20,
        fill=(255, 255, 255, 25)
    )
    
    # Draw box border
    overlay_draw.rounded_rectangle(
        [box_margin, box_top, width - box_margin, box_top + box_height],
        radius=20,
        outline=(255, 215, 0, 200),
        width=3
    )
    
    image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(image)
    
    # Invitation message
    y_text = box_top + 50
    invitation_lines = [
        "Buổi tiệc sinh nhật đáng nhớ",
        "Hãy cùng chia sẻ niềm vui và tạo nên",
        "những khoảnh khắc đẹp trong ngày đặc biệt này"
    ]
    
    for line in invitation_lines:
        bbox = draw.textbbox((0, 0), line, font=subtitle_font)
        line_width = bbox[2] - bbox[0]
        draw.text((center_x - line_width//2, y_text), line, 
                 font=subtitle_font, fill=(240, 240, 240))
        y_text += 55
    
    # Decorative divider in box
    y_text += 20
    divider_width = 250
    draw.line([center_x - divider_width//2, y_text, center_x + divider_width//2, y_text], 
              fill=(255, 215, 0), width=2)
    
    # Event details
    y_text += 50
    details = [ 
        ("Thời gian", "20:00 | 17/01/2025"),
        ("Địa điểm", "Đỉnh Phong Quán")
    ]
    
    for label, value in details:
        # Label
        label_bbox = draw.textbbox((0, 0), label, font=small_font)
        label_width = label_bbox[2] - label_bbox[0]
        draw.text((center_x - label_width//2, y_text), label, 
                 font=small_font, fill=(180, 180, 180))
        y_text += 45
        
        # Value
        value_bbox = draw.textbbox((0, 0), value, font=detail_font)
        value_width = value_bbox[2] - value_bbox[0]
        draw_text_with_shadow(draw, (center_x - value_width//2, y_text), value, 
                             detail_font, (255, 215, 0), (0, 0, 0, 100), shadow_offset=(2, 2))
        y_text += 80
    
    # Bottom decorative line
    bottom_y = 1420
    bottom_line_width = 350
    draw.line([center_x - bottom_line_width//2, bottom_y, center_x + bottom_line_width//2, bottom_y], 
              fill=(255, 215, 0), width=2)
    
    # RSVP message
    rsvp_text = "Rất hân hạnh được đón tiếp"
    rsvp_bbox = draw.textbbox((0, 0), rsvp_text, font=subtitle_font)
    rsvp_width = rsvp_bbox[2] - rsvp_bbox[0]
    draw.text((center_x - rsvp_width//2, 1460), rsvp_text, 
              font=subtitle_font, fill=(220, 220, 220))
    
    return image

def main():
    """Main function to generate the invitation card"""
    print("Generating birthday invitation card...")
    
    # Create the invitation
    invitation = create_birthday_invitation()
    
    # Save the image
    output_filename = "birthday_invitation.png"
    invitation.save(output_filename, quality=95)
    
    print(f"✅ Birthday invitation card saved as '{output_filename}'")
    print(f"   Card size: {invitation.width}x{invitation.height} pixels")

if __name__ == "__main__":
    main()
