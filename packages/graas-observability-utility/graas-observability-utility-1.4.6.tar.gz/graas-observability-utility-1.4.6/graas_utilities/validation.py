import json
import os
import jsonschema
from ref_Resolver import ExtendedRefResolver
from configs import mappingObject
from pkg_resources import resource_filename


def executeValidateJson(data, schema):
    try:
        jsonschema.validate(
            data,
            schema,
            resolver=ExtendedRefResolver(
                base_uri=f"{os.path.abspath(os.curdir)}/Schema",
                referrer=schema,
            ),
        )
    except jsonschema.exceptions.ValidationError as err:
        return {"status": "SCHEMA_VALIDATION_FAILED", "message": err.message}
    return {
        "status": "SCHEMA_VALIDATION_SUCCESS",
        "message": "Schema successfully validated",
    }


def extract_data_from_file(schema_file):
    path_for_schema = f"{os.path.abspath(os.curdir)}/Schema"

    with open(f"{path_for_schema}/{schema_file}.json", "r") as schema_file:
        schemaObj = json.load(schema_file)

    return schemaObj


def validateJson(dataJsonString, reportType):
    # Temporary fix for report type exceptions
    arrExceptions = [
        "amazon_onsiteSponsoredProductsCampaign",
        "amazon_storeKeyMetrics",
        "amazon_storeKeyMetricsMonthly",
        "amazon_storeKeyMetricsMonthlyBackFill",
        "shopee_productSponsoredAffiliateReport",
        "shopee_onsiteCampaign",
        "shopee_onsiteCampaignAfterReturnPeriod",
        "shopee_onsiteKeyword",
        "shopee_marketingShippingFeePromotion",
        "shopee_marketingShippingFeePromotionMonthly",
        "shopee_marketingShippingFeePromotionMonthlyBackFill",
        "shopee_storeKeyMetricsMonthlyBackFill",
        "lazada_storeKeyMetrics",
        "lazada_storeKeyMetricsMonthly",
        "lazada_storeKeyMetricsMonthlyBackFill",
        "lazada_onsiteKeyword",
        "flipkart_storeRevenue",
        "flipkart_PLAConsolidatedFSNSellerPortal",
        "flipkart_BrandAdsCampaign",
        "flipkart_DisplayAdsCampaign",
        "flipkart_PLAConsolidatedFSN",
        "flipkart_PCACampaign",
        "flipkart_PLACampaign",
        "flipkart_PLACampaignSellerPortal",
        "flipkart_searchTrafficReport",
        "flipkart_PCAProductPagePerformance"
    ]

    if reportType is None or not reportType:
        return {
            "status": "SCHEMA_VALIDATION_FAILED",
            "message": "Report type is Empty or None please enter valid string value!"
        }
    elif reportType in arrExceptions:
        return {
            "status": "SCHEMA_VALIDATION_SUCCESS",
            "message": "Schema successfully validated"
        }

    schema_file = mappingObject.get(reportType, "")

    if schema_file:
        try:
            jsonObject = json.loads(dataJsonString)
        except Exception as err:
            print("Error in converting data from string to json", err)
            return {
                "status": "FILE_FAILED_TO_CONVERT_JSON",
                "message": "Invalid JSON format"
            }
        if jsonObject:
            schemaObject = extract_data_from_file(schema_file)
            isValidated = executeValidateJson(jsonObject, schemaObject)
            return isValidated
        else:
            return {
                "status": "SCHEMA_VALIDATION_FAILED",
                "message": "Object is empty please enter correct object"
            }
    else:
        # Temporary fix
        return {
            "status": "SCHEMA_VALIDATION_SUCCESS",
            "message": "Schema successfully validated"
        }

answer = validateJson(
        json.dumps(
            {
                "merchantID": "TC1",
                "siteNickNameId": "shopee-4",
                "countryCode": "SG",
                "currencyCode": "SGD",
                "result": [
                    {
                        "Date": "14-02-2024",
                        "Campaign_Name": "Graas Caltrate keywords",
                        "Campaign_ID": 101100012592181,
                        "Campaign_Type": "Standard",
                        "Placement": "All - Sponsored Products",
                        "Budget": {
                            "amount": 5000,
                            "currencyCode": "MYR"
                        },
                        "Spend": {
                            "amount": 141,
                            "currencyCode": "MYR"
                        },
                        "Impression": 286,
                        "Clicks": 3,
                        "CTR": 1.05,
                        "CPC": {
                            "amount": 47,
                            "currencyCode": "MYR"
                        },
                        "Store_Add_To_Cart_Units": 0,
                        "Store_Orders": 0,
                        "Store_CVR": 0.0,
                        "Store_Units_Sold": 0,
                        "Store_Revenue": {
                            "amount": 0,
                            "currencyCode": "MYR"
                        },
                        "Store_ROI": 0.0,
                        "Direct_Add_To_Cart_Units": 0.0,
                        "Direct_Orders": 0,
                        "Direct_CVR": 0.0,
                        "Direct_Units_Sold": 0,
                        "Direct_Revenue": {
                            "amount": 0,
                            "currencyCode": "MYR"
                        }
                    }
                ]
            }
        ),
        "lazada_sponsoredDiscoveryReport",
    )
print(answer)